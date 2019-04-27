#!/usr/bin/python2

import hal, time


h = hal.component("therm_unify")
#a input pin for every setpoint
#a output pin for every temp

h.newpin("input.0", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("input.1", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("output" , hal.HAL_FLOAT, hal.HAL_OUT)


h.ready()
try:
  h["error"]=False
  while 1:
    if( old0 != h["input.0"]):
      h["output"] = h["input.0"]
    if( old1 != h["input.1"]):
      h["output"] = h["input.1"]
    old0 = h["input.0"]
    old1 = h["input.1"]

    time.sleep(1)

except KeyboardInterrupt:
    raise SystemExit
