import json

filename = "username.json"
try:
    with open(filename, "r") as file_obj:
        name = json.load(file_obj)
        print("Hey there, Joshua!")
    file_obj.close()
except FileNotFoundError:
    name = input("Could not find your name in the system. Please give your name! ")
    with open(filename, "w") as file_obj:
        json.dump(name, file_obj)
    file_obj.close()
    print("Ok, " + name + ", your name has been successfully added to the system!")
