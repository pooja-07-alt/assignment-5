dict={"alex": 85, "eric": 90, "rain": 72}
name=input("enter student name:")
if name in dict:
    print(f"{name} marks :",dict[name])
else:
    print("student not found")