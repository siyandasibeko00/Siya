options = ["Istanbul", "Paris", "Bangkok"]
print(options)
while True:
    city_flight = input("Select holiday destination from options provided {options}: ")

    if city_flight in options:
        print(f"Holiday destination: {city_flight}")
        break
    else:
        print("Input invalid! Please select from listed options")

num_nights = int(input("Number of nights staying at hotel: "))
rental_days = int(input("How many days will be hiring a car: "))

def hotel_cost(pricehotel = 2400, nights = num_nights):
 totalhotel = pricehotel * nights
 print(f"Total cost of hotel: {totalhotel}")
multiply_hotel = hotel_cost()

if city_flight == "Istanbul":
   
    def plane_cost(city_flight = 12000, two_flights = 2):
            total_flights_istanbul = city_flight * two_flights
            print(f"Total cost of flights to Istanbul: {total_flights_istanbul}")
    multiply_flights = plane_cost()

elif city_flight == "Paris":
    def plane_cost(city_flight = 14500, two_flights = 2):
            total_flights_paris = city_flight * two_flights
            print(f"Total cost of flights to Paris: {total_flights_paris}")
    multiply_flights = plane_cost()

else:
     def plane_cost(city_flight = 10500, two_flights = 2):
            total_flights_bangkok = city_flight * two_flights
            print(f"Total cost of flights to Bangkok: {total_flights_bangkok}")
multiply_flights = plane_cost()

def car_rental(price_rental = 750, rental = rental_days):
 total_rental = price_rental * rental
 print(f"Total cost of rental car: {total_rental}")
multiply_rental = car_rental()

def holiday_cost(num_nights, city_flight, rental_days):
    total_holiday = num_nights + city_flight + rental_days
    return (description + str(total_holiday))

hotel_cost
plane_cost
car_rental
description = "Total cost of holiday: "

sum = holiday_cost(hotel_cost, plane_cost, car_rental)

print(sum)