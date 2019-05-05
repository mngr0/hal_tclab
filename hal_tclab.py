#!/usr/bin/python2

import hal, time
import tclab
h = hal.component("hal_tclab")
#a input pin for every setpoint
#a output pin for every temp
setpoints=[0,0,0,0,0]
for i in range(4):
  h.newpin("setpoint-"+str(i), hal.HAL_FLOAT, hal.HAL_IN)
  h.newpin("temperature-"+str(i), hal.HAL_FLOAT, hal.HAL_OUT)
  #h.newpin("enable-"+str(i),hal.HAL_BIT, hal.HAL_IN)
  h.newpin("error-"+str(i), hal.HAL_BIT, hal.HAL_OUT)
  h["temperature-"+str(i)] = 0
  h["setpoint-"+str(i)] = 0
  #h["enable-"+str(i)] = False
  h["error-"+str(i)]= False

h.newpin("error", hal.HAL_BIT, hal.HAL_OUT)
h["error"] = 0
tc=tclab.TCLab()

h.ready()

try:
  h["error"]=False
  while 1:
    try:
      for i in range(4):
        h["temperature-%s"%str(i)]=tc.temperature(i)
        tmp_set = h["setpoint-%s"%str(i)]
        if tmp_set != setpoints[i]:
          tc.setpoint(i,tmp_set)
          setpoints[i] = tmp_set
        if tmpset>10:
          tc.enable(i)
          h["error-"+str(i)] = False
        else:
          tc.disable(i)
          h["error-"+str(i)] = True
      time.sleep(1)
    except:
     h["error"] = True

except KeyboardInterrupt:
    raise SystemExit
