#!/usr/bin/env python3
from sys import stdout
from time import sleep
from psutil import sensors_temperatures, virtual_memory, cpu_percent
from json import dumps
# if "PYDEBUG" not in os.environ.keys():
#     os.environ["PYDEBUG"]="on"

# with open(str(os.getenv("HOME"))+"/pylog","a") as f:
#     f.write("\n"+text+"time widget: output: "+json.dumps(output))
# for sadx in [1]:
state=1
while True:
    if state==1:
        temp=sensors_temperatures()
        mem = int(virtual_memory()[2])
        
        temps=[]
        for x in temp:
            for val in temp[x]:
                # print(type(val),x,val.current)
                temps.append(val.current)
        


        mtemp=round(max(temps),1)
        
        text=f"C: {cpu_percent()}%  M: {mem}%  : {mtemp}°C"
        text=f'{text}'
        output={"text": text}
        stdout.write(dumps(output)+"\n")
        stdout.flush()
    sleep(1)