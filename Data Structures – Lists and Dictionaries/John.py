list_of_names = []

while True:
    enter_name = input("Please enter a name: ")

    if enter_name == "John".lower().upper() or enter_name == "John":
        break
    else: 
        list_of_names.append(enter_name)

print(list_of_names)