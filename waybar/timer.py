import sys
import time
import json
import datetime
import os
# f = open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json")
while True:
    now=datetime.datetime.now()
    with open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json") as f:
        target=json.loads(f.read())


    if int(f'{target["hour"]:02}{target["minute"]:02}{target["second"]:02}')>int(f'{now.hour+2:02}{now.minute:02}{now.second:02}'):
        formatted=f'{((target["hour"]-now.hour)-3)%24}:{(target["minute"]-now.minute)%60}:{(target["second"]-now.second) %60}\n'
        sys.stdout.write(formatted)
    else:
        sys.stdout.write("Timer\n")
    sys.stdout.flush()
    time.sleep(1)
