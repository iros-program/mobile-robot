"""
Intelligent Robot System (i-ros.com)
"""
import platform
import serial
import time

"""
      COMMAND DESCRIPTION
In each command sent to robot, for example "Back;200;Back;200;200"
- First wheel :"Back" order at speed 200
- Second wheel: "Back" at speed 200
- The last param, time of execution is 300 (about 0.2 seconds)
""" 
class irosMobileRobot:
  TRY_NUM = 20
  robot   = None
  def __init__(self):
    for idx in range(0, self.TRY_NUM):
      try:
        if (platform.system() == "Windows"):
          ser = "COM%s" % idx
        elif (platform.system() == "Linux"):
          ser = "/dev/ttyUSB%s" % idx

        self.robot = serial.Serial(ser , 9600, timeout=0.1)
        break
      except:
        pass

  """
  greet robot with handshake
  """
  def greet(self):
    if self.robot == None:
      return False
      
    self.robot.reset_input_buffer()
    # handshake, try in TRY_NUM times
    self.robot.write(b"Start\n") 
    cnt = 0
    while cnt < self.TRY_NUM:      
      control = self.robot.readline().decode('utf-8',errors='ignore').rstrip()
      if control == "Start":
        return True
      # continue sending a handshake signal  
      self.robot.write(b"Start\n")
      cnt += 1
      time.sleep(0.2)

    return False
  
  """stop immediately (like brake)"""
  def stop(self):
    self.robot.write(b"Stop\n")
 
  """reduce speed to zero"""
  def pause(self):
    self.robot.write(b"Pause\n")
    
  """go back"""
  def back(self, speed = 200, duration = 200):
    # send command to the robot
    cmd = "Back;%s;Back;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)
    
  """go forward"""
  def forward(self, speed = 200, duration = 200):
    # send command to the robot
    cmd = "Forward;%s;Forward;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)
    
  """rotate to the left"""    
  def left(self, speed = 200, duration = 200):
    # send command to the robot
    cmd = "Back;%s;Forward;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)   

  """rotate to the right"""
  def right(self, speed = 200, duration = 200):
    # send command to the robot
    cmd = "Forward;%s;Back;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)   

  """receive message from robot"""        
  def response(self):
    return self.robot.readline().decode('utf-8',errors='ignore').rstrip()
