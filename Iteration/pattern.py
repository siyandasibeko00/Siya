user_number = int(input("Please enter a number between 1 - 5: "))
if user_number < 4:
        stars = "*"
for i in range(0, 4):
        print(stars)
        stars = stars + "*"
for i in range(4):
        print(stars)
        stars = stars - "*"

else:
    stars = "*"
    for i in range(4):
        stars_five = stars + "****"
        print(stars_five)
        stars_five = stars_five - stars