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
  FORWARD = 0
  BACK    = 1
  LEFT    = 2
  RIGHT   = 3
  robot   = None
  action  = ""
  def __init__(self):
    for idx in range(0, self.TRY_NUM):
      try:
        if (platform.system() == "Windows"):
          ser = "COM%s" % idx
        elif (platform.system() == "Linux"):
          ser = "/dev/ttyUSB%s" % idx

        self.robot = serial.Serial(ser , 9600, timeout=0.1)
        if self._greet():
          break
        else:
          self.robot = None
      except:
        pass

  """
  greet robot with handshake
  """
  def _greet(self):
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
  def back(self, speed = 200, duration = 100):
    # send command to the robot
    cmd = "Back;%s;Back;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)
    
  """go forward"""
  def forward(self, speed = 200, duration = 100):
    self.action = self.FORWARD
    # send command to the robot
    cmd = "Forward;%s;Forward;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)
    
  """rotate to the left"""    
  def left(self, speed = 200, duration = 100):
    self.action = self.BACK
    # send command to the robot
    cmd = "Back;%s;Forward;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)   

  """rotate to the right"""
  def right(self, speed = 200, duration = 100):
    self.action = self.RIGHT
    # send command to the robot
    cmd = "Forward;%s;Back;%s;%s\n" % (speed,speed,duration)
    cmd = bytes(cmd, encoding='utf-8')

    self.robot.write(cmd)   

  """control by joystick"""
  def jcommand(self, jcmd = [], duration = 100):
    if len(jcmd) < 4:
      return False
      
    # flush input buffer
    self._flush()  
    
    if (jcmd[0] > 0 and jcmd[1] == 0 
      and jcmd[2] == 0 and jcmd[3] == 0):
      # forward only
      self.action = self.FORWARD
      cmd = "Forward;%s;Forward;%s;%s\n" % (int(jcmd[0]), int(jcmd[0]), duration)
      cmd = bytes(cmd, encoding='utf-8')
      self.robot.write(cmd)   
    elif (jcmd[0] == 0 and jcmd[1] > 0 
      and jcmd[2] == 0 and jcmd[3] == 0):
      # back
      self.action = self.BACK
      cmd = "Back;%s;Back;%s;%s\n" % (int(jcmd[1]), int(jcmd[1]), duration)
      cmd = bytes(cmd, encoding='utf-8')
      self.robot.write(cmd)   
    elif (jcmd[0] == 0 and jcmd[1] == 0 
      and jcmd[2] > 0 and jcmd[3] == 0):
      if self.action == self.BACK:
        # back-left
        cmd = "Back;%s;Back;%s;%s\n" % (int(jcmd[2]), 0, duration)
        cmd = bytes(cmd, encoding='utf-8')
        self.robot.write(cmd)
      else:
        # forward-left 
        cmd = "Forward;%s;Forward;%s;%s\n" % (int(jcmd[2]) , 0, duration) 
        cmd = bytes(cmd, encoding='utf-8')
        self.robot.write(cmd)

    elif (jcmd[0] == 0 and jcmd[1] == 0 
      and jcmd[2] == 0 and jcmd[3] > 0):
      if self.action == self.BACK:
        # back-right 
        cmd = "Back;%s;Back;%s;%s\n" % (0, int(jcmd[3]), duration)
        cmd = bytes(cmd, encoding='utf-8')
        self.robot.write(cmd)   

      else:
        # forward-right
        cmd = "Forward;%s;Forward;%s;%s\n" % (0, int(jcmd[3]), duration)
        cmd = bytes(cmd, encoding='utf-8')      
        self.robot.write(cmd)
    # forward-left
    if (jcmd[0] > 0 and jcmd[2] > 0):
      self.action = self.FORWARD
      
      speedA = min(255, int(jcmd[0] + jcmd[2]))
      speedB = 255 - int(jcmd[2])
      
      cmd = "Forward;%s;Forward;%s;%s\n" % (speedA, speedB, duration) 
      cmd = bytes(cmd, encoding='utf-8')

      self.robot.write(cmd)   
    elif jcmd[0] > 0 and jcmd[3] > 0:
    # forward-right
      self.action = self.FORWARD
      
      speedA = 255 - int(jcmd[3])
      speedB = min(255, int(jcmd[0] + jcmd[3]))
      
      cmd = "Forward;%s;Forward;%s;%s\n" % (speedA, speedB, duration) 
      cmd = bytes(cmd, encoding='utf-8')    
      self.robot.write(cmd) 
    elif jcmd[1] > 0 and jcmd[2] > 0:
      # back-left
      self.action = self.BACK
      
      speedA = min(255, int(jcmd[1] + jcmd[2]))
      speedB = 255 - int(jcmd[2])
      
      cmd = "Back;%s;Back;%s;%s\n" % (speedA, speedB, duration)
      cmd = bytes(cmd, encoding='utf-8')    
      self.robot.write(cmd) 
    elif jcmd[1] > 0 and jcmd[3] > 0:
      # back-right
      self.action = self.BACK
      
      speedA = 255 - int(jcmd[3])
      speedB = min(255, int(jcmd[1] + jcmd[3]))
      
      cmd = "Back;%s;Back;%s;%s\n" % (speedA, speedB, duration)
      cmd = bytes(cmd, encoding='utf-8')    
      self.robot.write(cmd) 
    elif all(v == 0 for v in jcmd):
      if self.response() != "Pause":
        self.pause()

  """receive message from robot"""
  def response(self):
    return self.robot.readline().decode('utf-8',errors='ignore').rstrip()
  
  def _flush(self):
    bytesToRead = self.robot.inWaiting()
    self.robot.read(bytesToRead)