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
  h.newpin("enable-"+str(i),hal.HAL_BIT, hal.HAL_IN)
  h["temperature-%s"%str(i)] = 0
  h["setpoint-%s"%str(i)] = 0
  h["enable-"+str(i)] = 0

h.newpin("error", hal.HAL_BIT, hal.HAL_OUT)
tc=tclab.TCLab()

h.ready()

try:
  #try:
  h["error"]=False
  #except:
  #  h["error"]=True
  #  print ("no connection")
  #  raise SystemExit
  while 1:
    for i in range(4):
      h["temperature-%s"%str(i)]=tc.temperature(i)
      tmp_set = h["setpoint-%s"%str(i)]
      if tmp_set != setpoints[i]:
        tc.setpoint(i,tmp_set)
        setpoints[i] = tmp_set
        if tmpset>10:
          tc.enable(i)
        else:
          tc.disable(i)
    time.sleep(1)

except KeyboardInterrupt:
    raise SystemExit
