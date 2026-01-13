def bubble_sort(items):

    for i in range(len(items) - 1, -1, -1):
 
        for j in range(1, i + 1):
 
            if items[j - 1] > items[j]:
                items[j - 1], items[j] = items[j], items[j - 1]
    return items

example_list =  [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
sorted_list = bubble_sort(example_list)
print(sorted_list)

def binary_search(target, items):
    low, high = 0, len(items) - 1

    while high >= low:

        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1
 
        else:
            high = mid - 1

    return None

sorted_list
target_item = 9
result = binary_search(target_item, sorted_list)
if result is not None:
 print(f"Item {target_item} found at index {result}.")
else:
 print(f"Item {target_item} not found in the list.")

 #This algorithm is appropriate because it combines bubble sort to first order
 #the list in ascending order then comes the binary search to find the exact value
 #in the already sorted list

 def insertion_sort(item):
    for i in range(1, len(item)):
        key = item[i]
        j = i - 1
        while j >= 0 and key < item[j]:
            item[j + 1] = item[j]
            j -= 1
        item[j + 1] = key
    return item

unsorted_list =  [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
sorted_list_2 = insertion_sort(unsorted_list)
print(f"Sorted list: {sorted_list}")

def sequential_search(target, items):

    for index in range(len(items)):
        if items[index] == target:
            return index
 
    return None

sorted_list_2
target_item = 9
result = sequential_search(target_item, sorted_list_2)
if result is not None:
    print(f"Item {target_item} found at index {result}.")
else:
    print(f"Item {target_item} not found in the list.")

#The linear search method has been applied in this scenario
#this is used in real life when grocery shopping. One will move to every aisle to find every item on their list