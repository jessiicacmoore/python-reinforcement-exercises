def runner_stats(runner_id):
  print(f"How far (in meters) did runner {runner_id} run?")
  distance = float(input())
  print(f"How long did it take in minutes?")
  mins = float(input())

  secs = mins * 60
  return distance / secs

speed1 = runner_stats(1)
speed2 = runner_stats(2)
speed3 = runner_stats(3)

def determine_winner():
  
  if speed3 > speed2 and speed3 > speed1:
    return (f"Person 3 was the fastest at {speed3} m/s")

  elif speed2 > speed3 and speed2 > speed1:
    return (f"Person 2 was the fastest at {speed2} m/s")

  elif speed1 > speed3 and speed1 > speed2:
    return (f"Person 1 was the fastest at {speed1} m/s")

  elif speed1 == speed2 and speed2 == speed3:
    return (f"Everyone tied at {speed1} m/s")

def print_winner():
  print()
  print("----------")
  print(determine_winner())
  print()
  print()

print_winner()

