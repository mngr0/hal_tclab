#!/usr/bin/python2

from machinekit import hal
import time
import sys

#def create_therm_unify(name):

class therm_vcp:

  def __init__(self,name="therm_vcp"):
    self.h = hal.component(name)
    self.h.newpin("increase", hal.HAL_BIT, hal.HAL_IN)
    self.h.newpin("decrease", hal.HAL_BIT, hal.HAL_IN)
    self.h.newpin("setpoint-in", hal.HAL_FLOAT, hal.HAL_IN)
    self.h.newpin("setpoint-out" , hal.HAL_FLOAT, hal.HAL_OUT)
    self.h.ready()

  def routine(self):
    if self.h["increase"]:
      self.h["setpoint-out"] = self.h["setpoint-in"]+1
    if self.h["decrease"]:
      self.h["setpoint-out"] = self.h["setpoint-in"]-1




if __name__ == '__NOmain__':
  #check for  argc
  comp=therm_vcp(sys.argv[1])

#comp=therm_vcp(sys.argv[1])

#try:
#  while 1:
#    comp.routine()
#    time.sleep(1)
#except KeyboardInterrupt:
#  raise SystemExit
