from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import redis
import json
import random
from datetime import datetime

app = Flask(__name__)


redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='G@ry1111',
            database='test'
        )
    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection

def generate_tracking_report():
    connection = get_db_connection()
    report = {}
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT tracking_status, COUNT(*) as count FROM tracking_master GROUP BY tracking_status"
            cursor.execute(query)
            result = cursor.fetchall()

            expected_statuses = ["Created", "Package Received", "In Transit", "Out for Delivery", "Delivery Attempted", "Delivered", "Returned to Sender", "Exception"]
            report['trackingSummary'] = {status: 0 for status in expected_statuses}
            for status, count in result:
                if status in report['trackingSummary']:
                    report['trackingSummary'][status] = count
        except Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()
    report['created_dt'] = datetime.now().isoformat() + "Z"
    return report


def serialize_dates(package):
    # 將日期對象轉換為字符串
    if package.get('estimated_delivery') and not isinstance(package['estimated_delivery'], str):
        package['estimated_delivery'] = package['estimated_delivery'].strftime("%Y-%m-%d")
    if 'details' in package:
        for detail in package['details']:
            if detail.get('date') and not isinstance(detail['date'], str):
                detail['date'] = detail['date'].strftime("%Y-%m-%d")
    return package


@app.route('/query', methods=['GET'])
def query_package():
    sno = request.args.get('sno')

    cached_package = redis_client.get(sno)
    if cached_package:
        return jsonify({"status": "success", "data": json.loads(cached_package), "error": None})

    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT sno, tracking_status, estimated_delivery, recipient_id, current_location_id FROM tracking_master WHERE sno = %s", (sno,))
            package = cursor.fetchone()

            if package:
                cursor.execute("SELECT * FROM recipients WHERE id = %s", (package['recipient_id'],))
                recipient = cursor.fetchone()
                package['recipient'] = recipient

                cursor.execute("SELECT * FROM locations WHERE location_id = %s", (package['current_location_id'],))
                current_location = cursor.fetchone()
                package['current_location'] = current_location

                cursor.execute("SELECT * FROM tracking_details WHERE sno = %s ORDER BY date, time", (sno,))
                details = cursor.fetchall()
                package['details'] = details        

                del package['current_location_id']
                del package['recipient_id']

                package = serialize_dates(package)

                redis_client.setex(sno, 3600, json.dumps(package))

                response = {
                    "status": "success",
                    "data": package,
                    "error": None
                }
                return jsonify(response)
            else:
                return jsonify({"status": "error", "error": "Package not found"}), 404
        except Error as e:
            print("Error:", e)
            return jsonify({"status": "error", "error": "Internal Server Error"}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"status": "error", "error": "Database connection failed"}), 500

def generate_random_tracking_id():
    return random.randint(100000, 999999)

@app.route('/fake', methods=['GET'])
def generate_fake_data():
    num = int(request.args.get('num', 1))
    connection = get_db_connection()
    fake_data = []
    if connection:
        try:
            cursor = connection.cursor()
            for _ in range(num):
                sno = generate_random_tracking_id()
                status = random.choice(['Created', 'Package Received', 'In Transit', 'Out for Delivery', 'Delivery Attempted', 'Delivered', 'Returned to Sender', 'Exception'])
                estimated_delivery = datetime.now().strftime("%Y-%m-%d")
                recipient_id = random.randint(1234, 1251) 
                current_location_id = random.choice([1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 18, 19, 21, 23, 24])  


                cursor.execute("INSERT INTO tracking_master (sno, tracking_status, estimated_delivery, recipient_id, current_location_id) VALUES (%s, %s, %s, %s, %s)", (sno, status, estimated_delivery, recipient_id, current_location_id))

                cursor.execute("INSERT INTO tracking_details (sno, date, time, status, location_id) VALUES (%s, %s, %s, %s, %s)", (sno, estimated_delivery, '12:00', status, current_location_id))

                fake_data.append({"sno": sno, "tracking_status": status})
            connection.commit()
            response = {
                "status": "success",
                "data": fake_data,
                "error": None
            }
            return jsonify(response)
        except Error as e:
            print("Error:", e)
            return jsonify({"status": "error", "error": "Internal Server Error"}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"status": "error", "error": "Database connection failed"}), 500
@app.route('/generate_report', methods=['GET'])    
def report_route():
    report = generate_tracking_report()
    print(json.dumps(report, indent=2))  
    return jsonify(report)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
