#!/usr/bin/env python3
"""
  Switch controller program
  Intelligent Robot System (i-ros.com)
  Author:iros.program@gmail.com
"""
from utils.irosMobileRobot import *
import pygame
from pygame.locals import *
import time
      
def main() :
  mobile_robot = irosMobileRobot()
  # greet robot with handshake
  if (mobile_robot.greet() == False):
    print("Robot not found!")
    exit()
  
  pygame.init()
  jcmd    = [0, 0, 0, 0] # forward,back,right,left
  while True:
    eventlist = pygame.event.get()
    for e in eventlist:
      if e.type == JOYBUTTONDOWN:
        if e.button == 11:
          mobile_robot.action = mobile_robot.FORWARD
          print("Forward")
        if e.button == 12:
          mobile_robot.action = mobile_robot.BACK
          print("Back")
        if e.button == 14:
          mobile_robot.action = mobile_robot.RIGHT
          print("Right")
        if e.button == 13:
          mobile_robot.action = mobile_robot.LEFT
          print("Left")
      if e.type == JOYBUTTONUP:
        if e.button in [11,12,13,14]:
          print("Pause")
          mobile_robot.pause()
        if e.button == 5:
          print("Stop")
          mobile_robot.stop()
          time.sleep(2)
          exit()

      if e.type == JOYAXISMOTION:
        if e.axis == 3:
          # forward: -1.0, back: 1.0
          if e.value < 0:
            jcmd[0] = abs(e.value)*255
          elif e.value > 0:
            jcmd[1] = e.value*255
          else:
            jcmd[0], jcmd[1] = 0,0
            
        if e.axis == 2:
          # left: -1.0, right:1.0
          if e.value < 0:
            jcmd[2] = abs(e.value)*255
          elif e.value > 0:
            jcmd[3] = e.value*255
          else:
            jcmd[2],jcmd[3] = 0,0
    mobile_robot.jcommand(jcmd)
    if mobile_robot.action == mobile_robot.FORWARD:
      mobile_robot.forward()
    elif mobile_robot.action == mobile_robot.BACK:
      mobile_robot.back()
    elif mobile_robot.action == mobile_robot.RIGHT:
      mobile_robot.right()
    elif mobile_robot.action == mobile_robot.LEFT:
      mobile_robot.left()
    
    time.sleep(0.05)
 
if __name__ == '__main__':  
  # joystick
  pygame.joystick.init()
    
  try:
      joys = pygame.joystick.Joystick(0)
      joys.init()
      main()
  except pygame.error:
      print ('error has occured')
