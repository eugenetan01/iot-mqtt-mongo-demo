This demo allows you to write data to a local MQTT broker -> MongoDB Atlas 

There are 3 components:
1. mosquitto mqtt server
2. server.py running as the mqtt broker
3. pub.py to publish messages to the mqtt topic that the broker subs to

Note:
- Please ensure you have a .env file that looks like so:
  ```
  mongoc_conn="<your cluster uri>"
  ```
  
**Instructions**
__1. Install mosquitto__
- Run ```brew install mosquitto```

__2. Run the mosquitto MQTT server__
- Run ```mosquitto -v``` to start the server in verbose interactive mode

__3. Run the server.py file__
- Start the MQTT broker

__4. Run the pub.py file__
- publish a message to the sensors/data topic for the MQTT broker subbing to the topic to pick it up
- The JSON message looks something like so: {"sensor": "temperature", "value": 22.5, "timestamp": "2024-01-24T12:34:56"}

__5. Check the console__
- verify the json document was published to the MQTT broker

__6. Check MongoDB Atlas__
- check the iot_mqtt.mqtt collection in your atlas cluster to ensure the JSON doc was written successfully 
