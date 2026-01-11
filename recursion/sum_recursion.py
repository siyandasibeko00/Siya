list_of_integers = [1, 4, 5, 3, 12, 16]

def sum_of_integers(integers):
 
    if len(integers) == 0:
        return 0
    else:
        return integers[0] + sum_of_integers(integers[1:5])
    
print(f"Total of the added numbers in list is {sum_of_integers(list_of_integers)}")