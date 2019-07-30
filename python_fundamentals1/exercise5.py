distance_traveled = 0

while distance_traveled >= 0:

  print("Do you want to walk or run?")

  travel_mode = input()

  if travel_mode.lower() == "walk":
    distance_traveled += 1
  
  elif travel_mode.lower() == "run":
    distance_traveled += 5

  print("Distance from home is {}km.".format(distance_traveled))




