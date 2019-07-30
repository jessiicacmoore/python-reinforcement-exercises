# Retrieve user age
print("How old are you?")
user_age = int(input())

if int(user_age) <= 105:
  my_age = 26

  # if user is older
  if user_age >= my_age:
    print("You are {} years older than me.".format(user_age - my_age))

  # if user is younger
  else :
    print("You are {} years younder than me.".format(my_age - user_age))
else:
  print("I'm not sure I believe you.")