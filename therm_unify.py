#!/usr/bin/python2

import hal, time


h = hal.component("therm_unify")
#a input pin for every setpoint
#a output pin for every temp

h.newpin("in.0", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("in.1", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("out" , hal.HAL_FLOAT, hal.HAL_OUT)


h.ready()
try:
  old0 = h["in.0"]
  old1 = h["in.1"]
  while 1:
    if( old0 != h["in.0"]):
      h["out"] = h["in.0"]
    if( old1 != h["input.1"]):
      h["out"] = h["in.1"]
    old0 = h["in.0"]
    old1 = h["in.1"]

    time.sleep(1)

except KeyboardInterrupt:
    raise SystemExit
