#!/usr/bin/env python3
"""
  Turn right program
  Intelligent Robot System (i-ros.com)
  Author:iros.program@gmail.com
"""
from utils.irosMobileRobot import *
import time
  
if __name__ == '__main__':
  # greet robot with handshake
  mobile_robot = irosMobileRobot()
  if (mobile_robot == None):
    print("Robot not found!")
    exit()

  cnt = 0
  while cnt < 10:
    if cnt == 0:
      # rotate to the right at speed of 200, duration of 300
      mobile_robot.right(200, 300)
    
    # messages from the robot
    res = mobile_robot.response()
    if res:
      print(res)
            
    cnt += 1
    time.sleep(0.1)
    
  mobile_robot.stop()
