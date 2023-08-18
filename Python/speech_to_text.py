from flask import Flask, render_template, request
import paho.mqtt.client as mqtt
import requests

app = Flask(__name__)

# Configure MQTT broker connection
mqtt_broker = '44.195.202.69'
mqtt_port = 1883

# Define MQTT on_connect event handler
def on_connect(client, userdata, flags, rc):
    print('Connected to MQTT broker')
    client.subscribe('MY')

# Define MQTT on_publish event handler
def on_publish(client, userdata, mid):
    print('Message published to MQTT broker')

# Create MQTT client and configure event handlers
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.connect(mqtt_broker, mqtt_port, 60)

# Define Flask route for index page
@app.route('/')
def index():
    return render_template('speech_to_text.html')

# Define function to run command on the server and publish result to MQTT
def run_command_on_server():
    url = "https://rudraksh01.azurewebsites.net/"
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            result = response.text
            print("Response:")
            print(result)
            mqtt_client.publish('speech-to-text', result)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Define Flask route for MQTT publish
@app.route('/mqtt-publish', methods=['POST'])
def mqtt_publish():
    text = request.form.get('text')
    text = text.replace(" ", "")
    mqtt_client.publish('speech-to-text', text)
    return 'Message published to MQTT server'

if __name__ == '__main__':
    mqtt_client.loop_start()
    app.run(host='0.0.0.0', port=80)
