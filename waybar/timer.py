import sys
import time
import datetime
import os
if "targetTime.json" not in os.listdir(os.getenv("HOME")+"/dotfiles/waybar/"):
    with open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json","w") as f:
        f.write("0")
while True:
    with open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json") as f:
        target=int(float(f.read())-time.time())


    if target>0:
        hour=target//3600
        minute=(target%3600)//60
        second=target%60
        formatted=f'{hour:02}:{minute:02}:{second:02}\n'.replace("00:","",1)
        sys.stdout.write(formatted)
    else:
        sys.stdout.write("Timer\n")
    sys.stdout.flush()
    time.sleep(1)
