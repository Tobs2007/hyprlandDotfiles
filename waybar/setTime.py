import json
import os
import datetime
now=datetime.datetime.now()
h=int(input("h: "))
m=int(input("m: "))


if h<now.hour:
    date=now.day+1
else:
    date=now.day

out={
    "hour": h,
    "minute": m,
    "second": 0
}
with open(os.getenv("HOME")+"/dotfiles/waybar/targetTime.json","w") as f:
    json.dump(out,f)

