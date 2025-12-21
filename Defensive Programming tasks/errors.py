# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #Parenthesis added to define the print output
print("\n") #parenthesis added and indexation moved leftwards

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" #replaced == with = and lowercased the S and removed "years old"
age = int(age_str) #Lowercased s in the integer variable
print("I'm" + " " + age_str + " " + "years old.") #changed age to age_str

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #Removed quotation from the 3 to convert from string to integer
total_years = age + years_from_now
total_years_str = str(total_years) #coverted total_years into string

print("The total number of years: " + total_years_str) #parenthesis fixed and moved leftwards #changed answer_years into total_years

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 #total undefined variable replaced with total_years
total_months_str = str(total_months) #created a new line coverting total_months integer into string
print("In 3 years and 6 months, I'll be " + total_months_str + " months old") #changed total_months to total_months_str

#HINT, 330 months is the correct answer

