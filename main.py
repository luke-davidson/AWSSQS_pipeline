# Import dependencies
import boto3
import json
import psycopg2
from datetime import datetime
import hashlib

# Create sqs client
QUEUE_URL = 'http://localhost:4566/000000000000/login-queue'
sqs = boto3.client('sqs', endpoint_url=QUEUE_URL, region_name="us-east")

def mask(str):
    """
    Masking function for IP and Device ID

    Inputs:
        str (string): ip or device id
    Returns
        (string): hashed ip or device id
    """
    masked_data = hashlib.sha256()
    masked_data.update(str.encode())
    return masked_data.hexdigest()

def write_to_db(info):
    """
    Function to establish connection and write transformed data to a Postgres DB.

    Inputs:
        info (list): list of transformed data from SQS message
    """
    db_connection = psycopg2.connect(host="localhost", port=5432, database="postgres", user="postgres", password="postgres")
    cursor = db_connection.cursor()
    cursor.execute()
    cursor.execute("INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", info)
    
    db_connection.commit()
    cursor.close()
    db_connection.close()

# Main
if __name__ == "__main__":
    num_msgs = int(input(f"Enter the number of messages to add to the database: "))
    response = sqs.receive_message(QueueUrl=QUEUE_URL, MaxNumberOfMessages=num_msgs)
    if list(response.keys())[0] == "Messages":
        for m in response['Messages']:
            js = json.loads(m['Body'])
            if js == {'foo': 'oops_wrong_msg_type', 'bar': '123'}:
                print("[ERROR]: Wrong message type found. Skipping entry...")
            else:
                masked_ip = mask(js['ip'])
                masked_device_id = mask(js['device_id'])
                app_version = int(js['app_version'].replace(".", ""))
                info = [js['user_id'], js['device_type'], masked_ip, masked_device_id, js['locale'], app_version, datetime.now()]
                write_to_db(info)
    else:
        print(f"[ERROR]: No message found in data. Skipping response...")