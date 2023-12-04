# restful-api

## 程式語言
- python作為開發端語言，並使用了 Flask 框架。

## 資料庫
- MySQL

## 開發和部署環境

- Docker 部署 Redis & MySQL,
- NGINX 作為Web伺服器和反向代理

##### 說明你的專案達成哪些需求及怎麼部署的，例如： 完成哪些功能、需求？ 快取做到什麼程度？ 排程工作的結果是否有儲存到 S3 或其他地方？

## 前置作業安裝

安裝docker

```bash
sudo apt update
sudo apt install docker.io
```

安裝redis

```bash
sudo docker pull redis
```

啟動redis

```bash
sudo docker run --name gary-redis -p 6379:6379 -d redis
```

> 
> 
> - 這裡，**`gary-redis`** 是您給容器指定的名稱，您可以將其更改為您喜歡的任何名稱。
> - **`d`** 參數表示以「分離模式」運行，即容器將在後台運行。
> - 如果您需要將 Redis 的端口映射到主機，可以添加 **`p`** 參數，如 **`p 6379:6379`**（這將把容器的 6379 端口映射到主機的 6379 端口

驗證redis

```bash
sudo docker ps
```

```bash
sudo docker exec -it gary-redis redis-cli
```

- Redis 基本指令
    
    當然可以下是一些基本命令的示例：
    
    ### SET 命令
    
    `SET` 命令用於在 Redis 中儲存一個鍵值對。例如：
    
    ```bash
    SET mykey "Hello"
    
    ```
    
    這個命令會在 Redis 中創建一個名為 `mykey` 的鍵，其值為 `"Hello"`。
    
    ### GET 命令
    
    `GET` 命令用於從 Redis 中獲取鍵的值。如果鍵存在，它會返回鍵的值；如果鍵不存在，它會返回 nil。例如：
    
    ```bash
    GET mykey
    
    ```
    
    如果 `mykey` 存在，這個命令將返回之前設置的 `"Hello"`。
    
    ### DEL 命令
    
    `DEL` 命令用於從 Redis 中刪除指定的鍵。例如：
    
    ```bash
    DEL mykey
    
    ```
    
    這個命令將刪除名為 `mykey` 的鍵。
    
    ### KEYS 命令
    
    `KEYS` 命令用於查找所有符合給定模式的鍵。例如：
    
    ```bash
    KEYS *
    
    ```
    
    這個命令將列出 Redis 中所有的鍵。
    
    ### 其他命令
    
    Redis 還支持許多其他命令，用於管理列表、集合、有序集合等數據結構。您可以在 [Redis 命令參考](https://redis.io/commands/) 中找到完整的命令列表和更詳細的說明。
    

---

# MYSQL

- docke 安裝mysql

```bash
sudo docker pull mysql
```

- 運行 MySQL 容器：

```bash
sudo docker run --name gary-mysql -e MYSQL_ROOT_PASSWORD=G@ry1111 -p 3306:3306 -d mysql
```

- 驗證mysql

```bash
sudo docker ps
```

```bash
sudo docker exec -it gary-mysql mysql -u root -p
```

# Backend - python ****Flask****

- ****Flask****
    - **輕量級**：Flask 是一個微框架，適合輕量級的應用和微服務。
    - **靈活性**：Flask 提供了更多的靈活性，您可以自由選擇要使用的組件，這對於簡單的 API 服務非常合適。
    - **容易上手**：對於新手來說，Flask 的學習曲線相對較低，更容易快速開發和部署。
    - **適合輕量級專案**：如果您的專案不需要 Django 提供的許多內建功能，如用戶管理系統、管理後台等，Flask 是一個很好的選擇。

## 安裝 Flask

```bash
sudo apt update
sudo apt install python3-flask
```

vim app.py

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,Gary!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 , debug = Ture)
```

### 上述解釋

Flask 應用程式的結構

1. **導入 Flask**：
    
    ```python
    from flask import Flask
    
    ```
    
    - 這一行代碼導入了 Flask 類。Flask 是一個 Python 框架，用於建立 web 應用程式。
2. **創建 Flask 應用實例**：
    
    ```python
    app = Flask(__name__)
    
    ```
    
    - 這行代碼創建了一個 Flask 應用實例。`__name__` 是一個 Python 特殊變量，它表示當前 Python 腳本的名稱。在這裡，它用來告訴 Flask 從哪裡開始加載相關資源（如模板文件、靜態文件等）。
3. **定義路由和視圖函數**：
    
    ```python
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    ```
    
    - `@app.route('/')` 是一個「裝飾器」，它告訴 Flask 該函數將回應哪個 URL 的請求。在這個例子中，裝飾器創建了一個路由以回應根 URL `"/"` 的請求。
    - `hello_world` 是一個視圖函數，當用戶訪問根 URL（即 `http://your_server_ip_or_domain:5000/`）時，這個函數將被調用。
    - 視圖函數返回的字符串 `'Hello, World!'` 是將要顯示在用戶瀏覽器中的響應。
4. **條件語句啟動服務器**：
    
    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    
    ```
    
    - 這部分代碼檢查是否是直接運行該腳本（而不是將其作為模塊導入）。
    - `app.run(host='0.0.0.0', port=5000)` 啟動 Flask 應用的開發服務器。
        - `host='0.0.0.0'` 告訴您的操作系統監聽所有公共 IP，這樣您的應用可以被外部訪問。
        - `port=5000` 指定服務器監聽的端口號。這是 Flask 應用默認的端口號。

## 運行Falsk

```bash
flask run --host=0.0.0.0 --port=5000
```

### 背景運行 

- 方法一： ****`nohup`****

```bash
nohup flask run --host=0.0.0.0 --port=5000 &
```

> **`nohup`**（"no hang up" 的縮寫）可以讓您在後台運行 Flask 應用，並將輸出重定向到一個文件中，即使終端被關閉應用也會繼續運行。
> 

使用 **`ps`** 命令查看與 Flask 應用相關的進程：

```bash
ps aux | grep flask
```

終止Flask

```bash
kill -9 PID
```
- 方法二： ****`screen`**** (目前此方式 方便觀察log 做除錯)

```bash
sudo apt install screen
```

```bash
screen
```

```bash
cd /home/ubuntu/my_flask_app
```

```bash
flask run --host=0.0.0.0 --port=5000
```

> 斷開 **`screen`** 會話，使用快捷鍵 **`Ctrl-A`** 然後按 **`D`**。
> 

> 要重新連接到會話，使用命令 **`screen -r`**。
> 

### 關於Flask 自動重新載入

要讓 Flask 在修改 `app.py` 後自動重新加載（reload），您需要啟用 Flask 的自動重載功能。這在開發過程中非常有用，因為它允許您對代碼進行更改並立即看到結果，無需手動重新啟動服務器。

### 啟用自動重載

- 方法一：

1. **設置環境變量**：
    - 在運行 Flask 應用之前，您可以設置 `FLASK_ENV` 環境變量為 `development`。這將自動啟用調試模式，其中包括自動重載和其他幾個方便的開發功能。
    - 在您的終端中，執行以下命令：
        
        ```bash
        export FLASK_ENV=development
        
        ```
        
2. **運行 Flask 應用**：
    - 然後像往常一樣運行您的 Flask 應用：
        
        ```bash
        flask run --host=0.0.0.0 --port=5000
        
        ```
        
    - 或者，如果您使用了 `FLASK_APP` 環境變量指定了應用：
        
        ```bash
        export FLASK_APP=app.py
        flask run --host=0.0.0.0 --port=5000
        
        ```
在開啟了開發模式後，每當您對 `app.py` 或其他相關文件進行更改時，Flask 會自動偵測到這些更改並重新啟動服務器，從而加載最新的代碼。

#### 注意事項

- 開啟自動重載（以及調試模式）僅建議在開發過程中使用。在生產環境中，這應該保持關閉，以避免潛在的安全風險。
- 當您完成開發並準備部署應用程序時，請確保將 `FLASK_ENV` 設置回 `production`，並關閉調試模式。

        
- 方法二：

1. **啟用自動重載**：

    -  debug = ture 啟用自動重載。
    -  debug = false 禁用自動重載。
    -  debug = 0 禁用自動重載。
    -  debug = 1 啟用自動重載。

2. **運行 Flask 應用**：

    - 然後像往常一樣運行您的 Flask 應用：




## 調整nginx

```bash
sudo vim /etc/nginx/sites-available/flask_app.conf
```

```bash
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

確保在 **`/etc/nginx/sites-enabled/`** 目錄下有指向您的配置文件的符號鏈接。

您可以使用以下命令來檢查：

```bash

ls -l /etc/nginx/sites-enabled/
```

如果缺少鏈接，您需要創建一個：

```bash

sudo ln -s /etc/nginx/sites-available/flask_app.conf /etc/nginx/sites-enabled/
```

---

安裝**mysql-connector-python**

```bash
sudo apt update
sudo apt install python3-pip
sudo pip install mysql-connector-python
```

vim app.py

```bash
from flask import Flask
import mysql.connector
from mysql.connector import Error

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

@app.route('/')
def hello_world():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        # 假设有一个表格 'test_table' 且其中有列 'message'
        cursor.execute("SELECT message FROM test_table;")
        message = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return f'Hello, Gary! Welcome to Flask. Message from MySQL: {message}'
    else:
        return 'Hello, Gary! Welcome to Flask. But Database connection failed.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
```

創建sql

```bash
use test;

CREATE TABLE tracking_info (
    sno VARCHAR(50) PRIMARY KEY,
    tracking_status VARCHAR(100),
    estimated_delivery DATE
);

CREATE TABLE tracking_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tracking_sno VARCHAR(50),
    date DATE,
    time TIME,
    status VARCHAR(100),
    location_id INT,
    location_title VARCHAR(100),
    FOREIGN KEY (tracking_sno) REFERENCES tracking_info(sno)
);
```

安裝Redis cli

```bash
pip install redis
```

修改app.py

```bash
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import redis
import json
import random
from datetime import datetime

app = Flask(__name__)

# Redis 连接配置
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

    # 尝试从 Redis 中获取缓存数据
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

                # 将数据存储到 Redis 缓存并设置过期时间（例如 1 小时）
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
    # 这是一个简单的示例，您可以根据需要调整
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
                recipient_id = random.randint(1234, 1251)  # 假定收件人ID范围
                current_location_id = random.choice([1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 18, 19, 21, 23, 24])  # 假定地点ID范围

                # 插入数据到 tracking_master 表
                cursor.execute("INSERT INTO tracking_master (sno, tracking_status, estimated_delivery, recipient_id, current_location_id) VALUES (%s, %s, %s, %s, %s)", (sno, status, estimated_delivery, recipient_id, current_location_id))

                # 添加假的追踪详情
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
```

---

## 報表

沒有另外寫腳本，改成打一個request 去print

```bash
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
```

跟 route

```bash
@app.route('/generate_report', methods=['GET'])    
def report_route():
    report = generate_tracking_report()
    print(json.dumps(report, indent=2))  
    return jsonify(report)
```

test

```bash
curl "http://52.199.200.114/generate_report"
```

## Crontab

```bash
sudo crontab -e
```

用curl 

```bash
0 0,8,16 * * * /usr/bin/curl http://localhost:5000/generate_report

## test 
#*/2 * * * * /usr/bin/curl http://localhost:5000/generate_report
```

```bash
sudo crontab -l
```

改時區

```bash
sudo timedatectl set-timezone Asia/Taipei
```

確認是否成功執行

寫個兩分鐘執行一次

```bash
## test 
*/2 * * * * /usr/bin/curl http://localhost:5000/generate_report
```

看 crontab log

```bash
tail -f  /var/log/syslog -n 5
```

看 flask log 也有成功被打到回應