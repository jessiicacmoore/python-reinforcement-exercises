secret_number = 7
 

# retrieve user number and convert ot integer
print("Pick a number!")
user_number = int(input())

if user_number == secret_number:
  print("You win!")
  
elif user_number == (secret_number + 1) or user_number == (secret_number - 1):
  print("So close!")

else:
  print("Sorry, try again.")



