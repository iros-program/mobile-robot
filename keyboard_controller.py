#!/usr/bin/env python3
"""
  Keyboard controller program
  Intelligent Robot System (i-ros.com)
  Author:iros.program@gmail.com
"""
from utils.irosMobileRobot import *
from pynput.keyboard import Listener, Key
from queue import Queue
import time

queue     = Queue()
MAX_QUEUE = 5

# The function that's called when a key is pressed
def on_press(key):  
  if queue.qsize() <= MAX_QUEUE:
    queue.put(key)

def clear_queue():
  with queue.mutex:
      queue.queue.clear()  
      
if __name__ == '__main__':
    mobile_robot = irosMobileRobot()
    # greet robot with handshake
    if (mobile_robot.greet() == False):
      print("Robot not found!")
      exit()
      
    # Create an instance of Listener
    listener = Listener(on_press=on_press)
    listener.start()
    
    previous_key = None
    while True:
      key = queue.get()
      
      if key == Key.left:
        print("Left")
        if previous_key != Key.left:
          clear_queue()
          previous_key = Key.left
        # rotate to the left at speed of 200, duration of 100
        mobile_robot.left(200, 100)

      if key == Key.right:
        print("Right")
        if previous_key != Key.right:
          clear_queue()
          previous_key = Key.right
        # rotate to the right
        mobile_robot.right(200, 100)

      if key == Key.down:
        print("Back")
        if previous_key != Key.down:
          clear_queue()
          previous_key = Key.down
        # go back 
        mobile_robot.back(200, 100)

      if key == Key.up:
        print("Forward")
        if previous_key != Key.up:
          clear_queue()
          previous_key = Key.up
        # go forward 
        mobile_robot.forward(200, 100)  
      if key == Key.esc:
        quit()
      
    mobile_robot.stop()