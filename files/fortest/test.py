import json
f=open("base.txt","r")
a=json.load(f)
for i in a.values():
    k=len(i)

print(a["data"][0]["username"])
print(a["data"][1]["username"])
