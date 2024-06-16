#!/usr/bin/env python3

import rospy
from jethexa_controller import client,build_in_pose, kinematics_api, jethexa
import socket
import threading
import math



class MovingNode:
     def __init__(self):
        rospy.init_node("moving_node", anonymous=True, log_level=rospy.INFO)
        self.jethexa = client.Client(self)
        self.jethexa_twist = jethexa.JetHexa(self)
     def forward(self):
        self.jethexa.traveling(
                  gait=1, 
                  stride=40.0,
                  height=15.0,
                  direction=0,
                  rotation=0.0,
                  time=1, 
                  steps=0, 
                  interrupt=True,
                  relative_height=False)
        rospy.loginfo("forward")
     def rotate(self):
        self.jethexa.traveling(
                  gait=1, 
                  stride=40.0, 
                  height=15.0, 
                  direction=0, 
                  rotation=0.5,
                  time=0.8, 
                  steps=0, 
                  interrupt=True,
                  relative_height=False)
        rospy.loginfo("rotate")
     def stop(self):
        rospy.loginfo("stop")
        self.jethexa.traveling(gait=0)
     def wave(self):
       
        duration = 0.03
        self.jethexa_twist.set_pose_base(build_in_pose.DEFAULT_POSE_M, 0.8)
        org_pose = tuple(build_in_pose.DEFAULT_POSE_M)
        rospy.sleep(0.8)
      
        for j in range(7, 20, 2):
            i = 90 
            j = min(15, j)
            while i <= 360 + 85:
                if i == 90 and j == 7:
                    t = 0.5
                else:
                    t = duration
                i += 4 + j * 0.30
                x = math.sin(math.radians(i)) * (0.018 * (j + ((i - 90) / 360) * 2))
                y = math.cos(math.radians(i)) * (0.018 * (j + ((i - 90) / 360) * 2))
                pose = kinematics_api.transform_euler(org_pose, (0, 0, 0), 'xy', (x, y), degrees=False)
                self.jethexa_twist.set_pose_base(pose, t)
                rospy.sleep(t)

       
        for j in range(15, 4, -3):
            i = 360 + 85
            while i >= 90:
                i += -(4 + j * 0.30)
                k = 360 + 90 - i + 90
                x = math.sin(math.radians(k)) * (0.018 * (j + (1 - (i - 90) / 360) * -3))
                y = math.cos(math.radians(k)) * (0.018 * (j + (1 - (i - 90) / 360) * -3))
                pose = kinematics_api.transform_euler(org_pose, (0, 0, 0), 'xy', (x, y), degrees=False)
                self.jethexa_twist.set_pose_base(pose, duration)
                rospy.sleep(duration)
       

     def reset(self):
        self.jethexa_twist.set_pose_base(build_in_pose.DEFAULT_POSE_M, 1)

def handle_client_connection(client_socket):
     while True:
            command=client_socket.recv(1024).decode()
            if not command:
                 break
            if command == "forward":
                node.forward()
            elif command == "stop":
                 node.stop()
            elif command == "dance":
                 node.wave()
                 node.reset()

     client_socket.close()


if __name__=="__main__":
     node=MovingNode()
      
     

     server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     server.bind(("192.168.149.1",65432))
     server.listen(5)
     print("Waiting for connection..")


     while not rospy.is_shutdown():
           client_socket,addr=server.accept()
           print(f"Accepted connection from {addr}")
           client_handler=threading.Thread(target=handle_client_connection,args=(client_socket,))
           client_handler.start()  
