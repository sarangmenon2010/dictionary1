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