print ("="*19)
print("==>Challenger029<==")
print ("="*19)
print("create a programme check the speed of a car and if it's over 80km/h issue a fine. \n"
      "For every 1km/h it exceeds, it must pay 7 reais. ")

km_allowed = 80

km_car = int(input("Enter the car's speed: "))
if km_car > 80:
      exceeding_speed = km_car-km_allowed
      fine_value = exceeding_speed * 7.
      print("You exceeded the speed limit of {}km/h, your speed was of {}km/h. So the amount of your fine will be ${}".format(km_allowed, km_car, fine_value))
else:
      print("The vehicle was within the limit of the road, its speed was {}km/h.".format(km_car))
