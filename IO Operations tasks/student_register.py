num_of_students = int(input("How many students are registering: "))

with open("ID numbers.txt", "w") as f:
 
 for i in range(num_of_students):
        f.write(input("Please enter each students ID:"))
        print(i+1)