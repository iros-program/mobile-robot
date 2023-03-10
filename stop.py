#!/usr/bin/env python3
"""
  Stop program
  Intelligent Robot System (i-ros.com)
  Author:iros.program@gmail.com
"""
from utils.irosMobileRobot import *
import time
  
if __name__ == '__main__':
    mobile_robot = irosMobileRobot()
    # greet robot with handshake
    if (mobile_robot.greet() == False):
      print("Robot not found!")
      exit()

    cnt = 0
    while cnt < 100:
      if cnt == 0:
        # go forward at speed of 200, duration of 300
        mobile_robot.forward(200, 3000)
      
      if cnt == 10:
        # stop when cnt = 10
        mobile_robot.stop()
        
      # messages from the robot
      res = mobile_robot.response()
      if res:
        print(res)
              
      cnt += 1
      time.sleep(0.1)
      
    mobile_robot.stop()