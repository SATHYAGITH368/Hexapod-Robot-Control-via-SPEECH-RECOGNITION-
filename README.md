# Hexapod-Robot-Control-via-SPEECH-RECOGNITION-

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

