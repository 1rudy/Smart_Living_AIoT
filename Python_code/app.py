import os
import base64
import time
import recognise
from flask import Flask, render_template, request, jsonify, redirect
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Specify the specific folder path for saving images
file_save_path = 'images'  # Removed the leading slash to make it a relative path

# Initialize the global message variable
global message
message = ''


def capture_and_recognize():
    # Implement a loop to keep capturing and recognizing until a face is matched
    # while True:
    data = request.get_json()
    image_data = data['image_data'].split(",")[1]

    # Decode the base64 image data and save it as a file
    filename = 'captured_image.jpg'
    file_path = os.path.join(app.root_path, file_save_path, filename)

    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(image_data))

    result = recognise.face(file_path)  # Perform face recognition on the saved image
    print(result)

    if result == "LOGIN SUCCESSFUL":
        return True
        # return render_template('index.html', text_to_print=result)
    else:
        return False
        # time.sleep(2)  # Wait for a few seconds before capturing the next image


@app.route('/save_image', methods=['POST'])
def save_image():
    global message

    try:
        # Call the capture_and_recognize function to continuously capture and recognize the face
        if capture_and_recognize():
            # Face matched, set the session result and return success message
            # session['result'] = True
            message = "Face Matched"
            return jsonify('speech_to_text.html')

        else:
            return render_template('index.html')

    except Exception as e:
        return jsonify({'error': 'Error saving the image.'}), 500


@app.route('/')
def index():
    return render_template('index.html', message=message)


@app.route('/speech_to_text')
def speech_to_text():
    return render_template('speech_to_text.html', message=message)


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


# Define Flask route for MQTT publish
@app.route('/mqtt-publish', methods=['POST'])
def mqtt_publish():
    text = request.form.get('text')
    text = text.replace(" ", "")
    mqtt_client.publish('speech-to-text', text)
    return 'Message published to MQTT server'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    mqtt_client.loop_start()

