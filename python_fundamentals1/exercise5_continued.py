distance_traveled = 0
energy = 10

while True:
  print("Do you want to walk or run or eat or quit?")
  travel_answer = input().lower()

  if energy <= 0 and travel_answer != "quit":
    print("Energy low")
    continue

  if travel_answer == "walk":
     distance_traveled += 1
     energy -= 1

  elif travel_answer == "run":
      distance_traveled += 5
      energy -= 3

  elif travel_answer == "quit":
    break

  elif travel_answer == "eat":
    energy += 5
  
  else:
    print("Sorry, I don't recognize that command")

  print("distance traveled is {}".format(distance_traveled))

  print("Your energy level is {}".format(energy))






