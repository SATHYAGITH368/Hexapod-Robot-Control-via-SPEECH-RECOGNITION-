# Hexapod-Robot-Control-via-SPEECH-RECOGNITION-
This project demonstrates a voice-controlled hexapod robot using Voix for voice recognition and socket programming for communication. The system consists of two main components: a server (test_microphone.py) and a client (speechcontrol.py). The server processes voice commands and sends them to the robot controller, which executes the corresponding actions.

## ROS
ROS (Robot Operating System) is an open-source framework designed to simplify the development of complex robotic systems. It provides a collection of tools, libraries, and conventions that facilitate tasks such as hardware abstraction, device drivers, communication between processes, and package management.

Key Concepts: Nodes: ROS implements a distributed computing architecture where functionality is divided into nodes. Nodes are independent processes that communicate with each other using ROS topics, services, and actions.

Topics: Nodes can publish messages to topics or subscribe to topics to receive messages. Topics enable asynchronous communication between nodes, allowing them to send and receive data (e.g., sensor data, control commands).

Services: Nodes can offer services that other nodes can call to request specific tasks. Services follow a request-response pattern and are useful for synchronous communication.

Actions: Actions extend the capabilities of services by allowing nodes to execute long-running tasks in a non-blocking manner. They provide feedback on task progress and can be preempted if necessary.

Packages: ROS packages are the basic unit of software in ROS. They contain libraries, executables, scripts, configuration files, and documentation needed to perform specific tasks.

## SOCKET PROGRAMMING OVERVIEW
Socket programming is a fundamental technology for network communication, enabling applications to connect, send, and receive data over a network. It uses the concept of sockets, which are endpoints for communication between machines or processes.

Key Concepts: Socket: A socket represents one endpoint of a two-way communication link between two programs running on the network. It includes an IP address and a port number.

Client-Server Model: Socket programming typically follows a client-server architecture:

## PROJECT COMPONENTS:
Server (test_microphone.py):

Uses Voix for voice recognition to capture and interpret voice commands.
Acts as a server, sending recognized commands to the client via socket communication.
Recognizes commands such as "forward," "rotate," and "dance."
Client (speech_control.py):

Runs on the hexapod robot and acts as a client, receiving commands from the server.
Executes movements and actions (forward, rotate, dance) based on received voice commands.
## REQUIREMENTS:
Hardware:

Hexapod robot with appropriate motor and control hardware.
Microphone connected to the device running test_microphone.py.
Software:

Python 3.x
Voix library for voice recognition
Socket library for network communication
ROS (optional, if using ROS for robot control)
## Setup and Usage
# Setting Up the Server
Install Dependencies:

Ensure Python and necessary libraries are installed:
bash
Copy code
pip install voix
Configure Microphone:

Connect and configure the microphone on the server device.
Run the Server:

Execute test_microphone.py to start the voice recognition server:
bash
Copy code
python3 test_microphone.py --host (host-ip- address) --port 65432 -m en-us


# Setting Up the Client
Install Dependencies:

Ensure Python and necessary libraries are installed on the hexapod robot.
Configure Robot Control:

Modify speech_control.py to interface with your hexapod robot's hardware.
Run the Client:

Execute speech_control.py on the hexapod robot to start the client:
bash
Copy code
python3 speechcontrol.py
## Communication Flow
Voice Command:

The user gives a voice command (e.g., "forward," "rotate," "dance").
test_microphone.py uses Voix to recognize the command and sends it to the client via socket.
Command Execution:

speech_control.py receives the command and translates it into robot movements.
The hexapod robot performs the specified action.

## Additional Resources
Voix Documentation
Python Socket Programming
Hexapod Robot Control

## HEXAPOD
![PHOTO-2024-06-16-19-34-35](https://github.com/SATHYAGITH368/Hexapod-Robot-Control-via-SPEECH-RECOGNITION-/assets/142714885/65e68d69-703e-4735-94e3-37eb2a4a65f1)
