import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv()
# MongoDB Atlas connection string
mongo_conn_string = os.getenv("mongo_conn")


# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("sensors/data")


def on_message(client, userdata, msg):
    print(f"{msg.topic} {str(msg.payload)}")
    # Connect to MongoDB and insert the message
    client = MongoClient(mongo_conn_string)
    db = client.iot_mqtt
    collection = db.mqtt
    message = json.loads(msg.payload.decode("utf-8"))
    collection.insert_one(message)


# Set up MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
