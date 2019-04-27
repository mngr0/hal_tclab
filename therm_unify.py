#!/usr/bin/python2

import hal, time
import sys

def create_therm_unify(name):



#import argparse
#print (str(sys.argv))
#h = hal.component(sys.argv[1])
  h = hal.component(name)
#a input pin for every setpoint
#a output pin for every temp

  h.newpin("in.0", hal.HAL_FLOAT, hal.HAL_IN)
  h.newpin("in.1", hal.HAL_FLOAT, hal.HAL_IN)
  h.newpin("out" , hal.HAL_FLOAT, hal.HAL_OUT)
  time.sleep(1)

  old0 = h["in.0"]
  old1 = h["in.1"]


  def therm_unify_routine():
    if( old0 != h["in.0"]):
      h["out"] = h["in.0"]
    if( old1 != h["in.1"]):
      h["out"] = h["in.1"]
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
