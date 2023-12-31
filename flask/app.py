from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import random

app = Flask(__name__)

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

@app.route('/query', methods=['GET'])
def query_package():
    sno = request.args.get('sno')
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # 查询 tracking_master 表
            cursor.execute("SELECT sno, tracking_status, estimated_delivery, recipient_id, current_location_id FROM tracking_master WHERE sno = %s", (sno,))
            package = cursor.fetchone()

            if package:
                # 收件人
                cursor.execute("SELECT * FROM recipients WHERE id = %s", (package['recipient_id'],))
                recipient = cursor.fetchone()
                package['recipient'] = recipient

                # 當前位置
                cursor.execute("SELECT * FROM locations WHERE location_id = %s", (package['current_location_id'],))
                current_location = cursor.fetchone()
                package['current_location'] = current_location

                # 物流歷史紀錄
                cursor.execute("SELECT * FROM tracking_details WHERE sno = %s ORDER BY date, time", (sno,))
                details = cursor.fetchall()
                package['details'] = details        

                del package['current_location_id']
                del package['recipient_id']


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


import random
from datetime import datetime


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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)