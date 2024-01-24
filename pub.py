import json
import paho.mqtt.publish as publish

# MQTT Broker details
broker_host = "localhost"
topic = "sensors/data"

# Your data
data = {"sensor": "temperature", "value": 22.5, "timestamp": "2024-01-24T12:34:56"}

# Convert data to JSON
json_data = json.dumps(data)

# Publish JSON data
publish.single(topic, json_data, hostname=broker_host)
