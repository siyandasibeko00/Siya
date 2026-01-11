largest_number_list = [3, 1, 6, 8, 2, 4, 5]

def largest_number(numbers):

    if len(numbers) == 1:
        return numbers[0]

    rest_of_list = largest_number(numbers[1: :1])
    
    first_number = numbers[0]
    
    if first_number > rest_of_list:
        return first_number
    else:
        return rest_of_list

maximum_number = largest_number(largest_number_list)
print(largest_number_list)
print(f"The largest number in the list is: {maximum_number}")
