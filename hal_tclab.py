#!/usr/bin/python2

from machinekit import hal
import time
import tclab

class hal_tclab:
  def __init__(self, name="hal_tclab"):
    print("HERE IS HAL_TCLAB STARITNG")
    self.h = hal.Component(name)
#a input pin for every setpoint
#a output pin for every temp
    self.setpoints=[0,0,0,0,0]
    for i in range(4):
      self.h.newpin("setpoint-"+str(i), hal.HAL_FLOAT, hal.HAL_IN)
      self.h.newpin("temperature-"+str(i), hal.HAL_FLOAT, hal.HAL_OUT)
      self.h.newpin("error-"+str(i), hal.HAL_BIT, hal.HAL_OUT)
      self.h["temperature-"+str(i)] = 0
      self.h["setpoint-"+str(i)] = self.setpoints[i]
      self.h["error-"+str(i)]= False
    self.h.newpin("enable",hal.HAL_BIT, hal.HAL_IN)
    self.h.newpin("error", hal.HAL_BIT, hal.HAL_OUT)
    self.h["error"] = 0
    self.tc=tclab.TCLab()
    self.h.ready()
    print("HERE IS HAL_TCLAB READY")


  def take(self):
    return self.h

  def routine(self):
    try:
      self.h["error"]=False
      while 1:
        self.h["error"]=False
        try:
          for i in range(4):
            self.h["temperature-"+str(i)]=self.tc.temperature(i)
            tmp_set = self.h["setpoint-"+str(i)]
            if tmp_set != self.setpoints[i]:
              self.tc.setpoint(i,tmp_set)
              self.setpoints[i] = tmp_set
            if self.h["enable"]:
              self.tc.enable(i)
            else:
              self.tc.disable(i)
        except Exception as e:
          self.h["error"] = True
          print (str(e))
    except Exception as e:
      print( str(e))
      raise SystemExit

print("HERE IS HAL_TCLAB MAIN")

comp= hal_tclab()
#hal.addf("servo-thread")
#try:
#  while 1:
#    comp.routine()
#    time.sleep(1)
#except Exception as e:
#  print (str(e))
#  raise SystemExit
