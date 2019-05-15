#!/usr/bin/python2

import hal, time
import sys

#def create_therm_unify(name):

class therm_unify:

  def __init__(self,name="therm_unify"):
    self.h = hal.component(name)
    self.h.newpin("in.0", hal.HAL_FLOAT, hal.HAL_IN)
    self.h.newpin("in.1", hal.HAL_FLOAT, hal.HAL_IN)
    self.h.newpin("out" , hal.HAL_FLOAT, hal.HAL_OUT)
    self.old0 = self.h["in.0"]
    self.old1 = self.h["in.1"]
    self.h.ready()

  def routine():
    if( old0 != h["in.0"]):
      h["out"] = h["in.0"]
    if( old1 != h["in.1"]):
      h["out"] = h["in.1"]
    old0 = h["in.0"]
    old1 = h["in.1"]


if __name__ == '__NOmain__':
  #check for  argc
  comp=therm_unify(sys.argv[1])


  h = hal.component(sys.argv[1])
  h.newpin("in.0", hal.HAL_FLOAT, hal.HAL_IN)
  h.newpin("in.1", hal.HAL_FLOAT, hal.HAL_IN)
  h.newpin("out" , hal.HAL_FLOAT, hal.HAL_OUT)
#time.sleep(1)
  old0 = h["in.0"]
  old1 = h["in.1"]

#export function
  h.ready()


  try:
    old0 = h["in.0"]
    old1 = h["in.1"]
    while 1:
      if( old0 != h["in.0"]):
        h["out"] = h["in.0"]
      if( old1 != h["in.1"]):
        h["out"] = h["in.1"]
      old0 = h["in.0"]
      old1 = h["in.1"]
      time.sleep(1)
  except KeyboardInterrupt:
    raise SystemExit
