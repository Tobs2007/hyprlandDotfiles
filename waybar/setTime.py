import json
import os
import time
import datetime
now=datetime.datetime.now()

timeobj=datetime.datetime.replace(now,hour=int(input("h: "))-2,minute=int(input("m: ")),second=0)

out=timeobj.timestamp()
with open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json","w") as f:
    f.write(str(out))

