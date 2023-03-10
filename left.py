#!/usr/bin/env python3
"""
  Turn left program
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
    while cnt < 10:
      if cnt == 0:
        # rotate to the left at speed of 200, duration of 300
        mobile_robot.left(200, 300)
      
      # messages from the robot
      res = mobile_robot.response()
      if res:
        print(res)
              
      cnt += 1
      time.sleep(0.1)
      
    mobile_robot.stop()
