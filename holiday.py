options = ["1 = Istanbul", "2 = Paris", "3 = Bangkok"]
print(options)

options_int = [1, 2, 3]

while True:
    city_flight = int(input("Select holiday destination from options provided {options_int}: "))

    if city_flight in options_int:
        print(f"Holiday destination: {city_flight}")
        break
    else:
        print("Input invalid! Please select from listed options")

num_nights = int(input("Number of nights staying at hotel: "))
rental_days = int(input("How many days will be hiring a car: "))

def hotel_cost(num_nights):
     return num_nights * 2400

if city_flight == "1":
   
    def plane_cost(city_flight):
            city_flight = 12000
            return city_flight * 2

elif city_flight == "2":
    def plane_cost(city_flight):
            city_flight = 14500
            return city_flight * 2            

else:
     def plane_cost(city_flight):
            city_flight = 10500
            return city_flight * 2

def car_rental(rental_days):
    return 750 * rental_days

def holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

total_cost = holiday_cost(num_nights, city_flight, rental_days)
print(f"Total cost of holiday: {total_cost}")