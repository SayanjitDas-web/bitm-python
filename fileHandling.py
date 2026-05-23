import json

with open("data.txt","r") as file:
    data = json.loads(file.read())
    print(type(data))
    file.close()