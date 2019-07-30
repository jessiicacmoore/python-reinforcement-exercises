names = ['Angela', 'Pamela', 'Sandra', 'Rita']

def check_list(user_name):
  if user_name in names:
    print(f"Welcome to the party {user_name}!")
  else:
    print(f"Who goes there?")

print("I need to see if you're on the list - tell me your name")
user_name = input()
check_list(user_name)