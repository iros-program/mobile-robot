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
  # greet robot with handshake
  mobile_robot = irosMobileRobot()
  if (mobile_robot == None):
    print("Robot not found!")
    exit()
  
  pygame.init()
  jcmd    = [0, 0, 0, 0] # forward,back,right,left
  pressed_button = ""
  while True:
    eventlist = pygame.event.get()
    for e in eventlist:
      if e.type == JOYBUTTONDOWN:
        if e.button == 11:
          pressed_button = "Forward"
          print("Forward")
        if e.button == 12:
          pressed_button = "Back"
          print("Back")
        if e.button == 14:
          pressed_button = "Right"
          print("Right")
        if e.button == 13:
          pressed_button = "Left"
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
      if e.type == JOYBUTTONUP:
        pressed_button = ""
        
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
    if pressed_button == "Forward":
      mobile_robot.forward()
    elif pressed_button == "Back":
      mobile_robot.back()
    elif pressed_button == "Right":
      mobile_robot.right()
    elif pressed_button == "Left":
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
