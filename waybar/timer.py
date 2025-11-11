#pyright: reportUnusedCallResult=false
import sys
import time
import os
home = os.getenv("HOME") or "/"

if "targetTime.json" not in os.listdir(home+"/dotfiles/waybar/"):
    with open(home+"/dotfiles/waybar/targetTime.json","w") as f:
        f.write("0")  
while True:
    with open(home+"/dotfiles/waybar/targetTime.json") as f:
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
