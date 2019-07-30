# ----- Name example -----

print("What is your name?")

user_name = input()

print("Hello, {}".format(user_name))


# ----- Password example -----

secret_password = "please"

print("What is the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))


# ----- Cookies example -----

print("How many cookies have been eaten?")
eaten = input()

# Convert eaten to integer and subtract is from 12
remaining_cookies = 12 - int(eaten)

# Print result
print("There are {} cookies left".format(remaining_cookies))


# ----- User age challenge -----

print("What is your age?")
# Retrieve user age and convert from string to integer
user_age = int(input())

print("What year is it now?")
# Retrieve current year and convert from string to integer
current_year = int(input())

# Print result
print("You were born in {}!".format(current_year - user_age))

