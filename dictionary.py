studentdetails = {
    "studentname": "Sarang Menon",
    "grade": 8,
    "school": "Cyboard School",
    "place": "Kerala"
}

print(studentdetails)
print(studentdetails.keys())
print(studentdetails.values())
print(studentdetails.items())

if "food" in studentdetails:
    print("it exists")
else:
    print("it doesn't exists")

if "food" not in studentdetails:
    print("it exists")
else:
    print("it doesn't exists")

studentdetails["place"] = "Hyderabad"
print(studentdetails)

sst = {
    "civics": "constitution of india",
    "history": "rural life under british india",
    "geography": "natural resources of the earth"
}

print(sst)

sst["civics"] = "indian judiciary"
print(sst)
sst["mathematics"] = "squares and square roots"
print(sst)
print(len(sst))
for i in sst:
    print(i)

for i in sst.values():
    print(i)

sst.pop("mathematics")
print(sst)
sst.popitem()
print(sst)
