# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #add quotation marks
animal_type = "cub"
number_of_teeth = 16
number_of_teeth_str = str(number_of_teeth) #coverted number_of_teeth into string

full_spec = "This is a " + animal + ". It is a " + number_of_teeth_str + " and it has " + animal_type + " teeth" #properly referenced variables by adding quoatations around non-variable strings

print(full_spec) #parenthesis

