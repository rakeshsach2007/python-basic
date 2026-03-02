import json

x = {"name":"Rakesh",
     "Age":41,
     "Job":"TCS"}

y = json.dumps(x,indent=3,separators=(",","="))

print(y)