#!/usr/bin/python2

import hal, time
import sys

#def create_therm_unify(name):

class therm_unify:

  def __init__(self,name="therm_unify"):
    print("HERE IS UNIFY STARTING")
    self.h = hal.component(name)
    self.h.newpin("in.0", hal.HAL_FLOAT, hal.HAL_IN)
    self.h.newpin("in.1", hal.HAL_FLOAT, hal.HAL_IN)
    self.h.newpin("out" , hal.HAL_FLOAT, hal.HAL_OUT)
    self.old0 = self.h["in.0"]
    self.old1 = self.h["in.1"]
    self.h.ready()
    print("HERE IS UNIFY READY")

  def routine(self):
    if( self.old0 != self.h["in.0"]):
      self.h["out"] = self.h["in.0"]
    if( self.old1 != self.h["in.1"]):
      self.h["out"] = self.h["in.1"]
    self.old0 = self.h["in.0"]
    self.old1 = self.h["in.1"]


if __name__ == '__NOmain__':
  #check for  argc
  comp=therm_unify(sys.argv[1])
print("HERE IS UNIFY MAIN")
print("argc=",len(sys.argv))
comp=therm_unify(sys.argv[1])
try:
  while 1:
    comp.routine()
    time.sleep(0.4)
except Exception as e:
  print(str(e))
  raise SystemExit
