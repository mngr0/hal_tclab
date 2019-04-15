#!/usr/bin/python
import hal, time
import tclab
h = hal.component("hal_tclab")
#a input pin for every setpoint
#a output pin for every temp
setpoints=[0,0,0,0,0]
for i in range(5):
    h.newpin("setpoint-%s"%str(i), hal.HAL_FLOAT, hal.HAL_IN)
    h.newpin("temperature-%s"%str(i)", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("error", hal.HAL_FLOAT, hal.HAL_OUT)
h.ready()
try:
    while 1:
        time.sleep(1)
        h['out'] = h['in']
        for i in range(5):
            h["temperature-%s"%str(i)]=tclab.temperature(i)
            tmp_set = h["setpoint-%s"%str(i)]
            if tmp_set != setpoints[i]:
                tclab.setpoint(i,tmp_set)
        #update required
except KeyboardInterrupt:
    raise SystemExit
