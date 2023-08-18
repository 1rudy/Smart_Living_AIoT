# Smart_Living_AIoT
## STORY
Smart Living [AIoT] is an IoT-based project to control home appliances through voice commands. IoT or the Internet of Things, is an upcoming technology that 
allows us to control hardware devices through the Internet. Here we propose to use IoT to control home appliances, thus automating modern homes through the
Internet using voice commands. Our user-friendly interface allows users to easily control lights, fans, TV, fridge, and AC pump. The home security system has
become vital for every house. It is important. Here we propose to use AI and IoT to assist users in improving the door security of sensitive locations by using face
detection and recognition.

## INTRODUCTION

Making homes even smarter is the goal of voice-based home automation systems. Voice commands and cell phones will be used to operate small appliances in the house. 
It will be easier to get by as a result. According to their needs, customers will be able to add or remove additional electronic devices using web applications.
There is a growing need for efficient and reliable communication between various smart devices within a household. These devices, such as smart lights, 
smart appliances, and sensors, need to exchange data and control commands seamlessly to create an intelligent and interconnected home environment. However, 
the challenge lies in establishing a robust communication protocol that is lightweight, low-power, and can handle a multitude of devices without causing network 
congestion. As a solution, adopting the MQTT protocol in home automation enables devices to easily publish and subscribe to specific topics, allowing them to share 
real-time data and execute control commands effectively. MQTT's efficiency, simplicity, and support for various IoT platforms make it an essential and indispensable
component in home automation systems, promoting a seamless and smarter living experience for homeowners.

## COMPONENTS
WIZnet-W5300 TOE SHIELD 
LEDs, Buzzers, Doors, fans, and any other electronic components
 
## SOFTWARE
PYCharm
Arduino IDE
MQTT Server
Flask Web Application

<img width="582" alt="image" src="https://github.com/1rudy/Smart_Living_AIoT/assets/118504450/9f8e0de5-9d0a-4448-b57a-eca0eacc281e">


## IDENTIFYING FACES:
The class Identifier in the app.py file contains the code to detect and recognize faces by using the face_recognition library. When the views call the check function and the image is passed, this function finds the faces in the image and the face encodings in the image. If the encodes match any of the encodings in images then the page will redirect to the next page. If none of the images match, the page will be the same. 

## SPEECH-TO-TEXT MODULE  
This web page is for speech-to-text conversion. The page contains a background image, a heading ("SPEAK HERE"), and a text area where users can speak something and see the text representation. There are two buttons: "Submit" to send the entered text for processing (presumably to a server), and "Voice Input" to initiate speech recognition. The JavaScript code uses the Web Speech API to enable voice recognition, allowing users to speak into the textarea. When the "Voice Input" button is clicked, the recognition starts, and the text result is displayed in the text area. The "Submit" button is used to send the text to the MQTT server using the Flask application.





