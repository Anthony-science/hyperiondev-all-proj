# Define hotel_cost function

def hotel_cost (a, hotel_rate):
    tot_hotel_cost = a * hotel_rate
    return tot_hotel_cost


# Define plane_cost function
def plane_cost (c):
    if city_flight == "paris" or "Paris":
        c = fl_paris
    elif city_flight == "berlin" or "Berlin":
        c = fl_berlin
    elif city_flight == "amsterdam" or "Amsterdam":
        c = fl_amsterdam
    else:
        print("Sorry, your city is not listed.")
    return c
       

# Define car_rental function
def car_rental (d, e):
    e = car_hire
    tot_rental = d * e
    return tot_rental


# Define total holiday_cost function
def holiday_cost (f, g, h):
    hol_cost = f + g + h
    return hol_cost


# Set fixed values for hotel and flights to each destination
hotel_rate = 100
car_hire = 75
fl_paris = 200
fl_berlin = 250
fl_amsterdam = 175

# Request user input (I included a while True loop
# so that the city could be typed with or without a capital letter
# and so that unlisted cities would not throw an error and crash the program)
while True:
    city_flight = input("Please enter your destination city (Paris, Berlin, or Amsterdam): ")
    if city_flight.strip().lower() in ['paris', 'berlin', 'amsterdam']:
        break
    print("Invalid input")
num_nights = int(input("Number of nights: "))
rental_days = int(input("Number of days of car rental: "))

# Call functions
f = hotel_cost (hotel_rate, num_nights)

g = plane_cost (city_flight)

h = car_rental (rental_days, car_hire)

i = holiday_cost (f, g, h)

# Output results
print(f"\n \nYour holiday costs are as follows: \n"  "Hotel cost: £" + (str(f)), "\nPlane cost: £" + (str(g)), "\nCar rental: £" + (str(h)), "\n \nTotal Holiday cost: £" + (str(i)))
