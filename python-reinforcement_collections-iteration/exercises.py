# ---------- EXERCISE ZERO ---------

# --- Lists
fav_colours = ['blue', 'teal', 'maroon']

family_ages = [26, 22, 34, 28]

coin_flip = ['heads', 'tails', 'heads', 'heads', 'tails']

fave_bands = ['Kings of Leon', 'The Killers', 'Blink-182']

# --- Dictionaries
words = {
  'nummet': 'light meal or luncheon',
  'behoof': 'a benefit resulting from some course of action',
  'stactometer': 'pipette with hollow bulb for counting drops'
}

movies = {
  'Jaws': 1975,
  'Empire Records': 1995,
  'The Conjuring': 2013
}

cities = {
  'Toronto': 2.93,
  'Brooklyn': 2.64,
  'Barcelona': 1.61
}

friend_ages = {
  'Rachel': 23,
  'Christina': 25,
  'Alan': 32,
  'Brandon':27
}



# ---------- EXERCISE ONE ---------

# Print out the list of coin flips.
print(coin_flip)

# Print out the first element of the list of your favourite colours.
print(fav_colours[0])

# Output the sorted version of the list of your friends and family members' ages.
family_ages.sort()
print(family_ages)

# Add a new baby (0 years old) to the list of your family's ages.
family_ages.append(0)
# print(family_ages)

print(movies['The Conjuring'])



# ---------- EXERCISE TWO ---------

# Print out the last element of the list of your favourite colours.
print(fav_colours[-1])

# Add a new city to the dictionary of cities and population.
cities['Paris'] = 2.14
# print(cities)

# Reverse the list of coin flips and save it.
coin_flip.reverse()
# print(coin_flip)

# Print out the population of one of the cities.
print(cities['Paris'])

# Print out a sentence about each item in the list of performing artists. For example:
for band in fave_bands:
  print(f"I think {band} is great.")



# ---------- EXERCISE THREE ---------

# Print out the first two performing artists in that list.
print(fave_bands[0:2])

# For each of your favourite movies, print out a sentence about when the movie was released.
for movie, year in movies.items():
  print(f"{movie} came out in {year}")

# Sort and reverse the list of ages of your family. Save it and print it to the screen.
family_ages.sort(reverse=True)
print(family_ages)

# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.
movies['Beauty and the Beast'] = {
  'original': 1991,
  'remake': 2017
}
print(movies)



# ---------- EXERCISE FOUR ---------

# Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
for name, age in friend_ages.items():
  if age > 30:
    print(f"{name} is {age}")
  else:
    print(f"{name} is not 30")

# Find and output the age of the oldest person in your friends/family list.
print(family_ages[0])

# Count how many times you flipped 'heads' using the coin flips list.
print(coin_flip.count('heads'))

# You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
fave_bands.pop(1)
print(fave_bands)

# Pick a city in your city population dictionary and change its population.
cities['Brooklyn'] = 2.75
print(cities)

# ---------- EXERCISE FIVE ---------

# Find the sum total of the population in the dictionary of cities.
total_population = 0

for city, pop in cities.items():
  total_population += pop

print(total_population)

# Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age. For example:
for name, age in friend_ages.items():
  if age > 25:
    print(f"{name} is {age}, therefore they're old")
  else:
    print(f"{name} is {age}, therefore they're young")

# Print out the last two colours in your list of favourite colours.
print(fav_colours[-1] + ", " + fav_colours[-2])

# Increase by 1 the age of everyone in your list of ages. Print it out.
for name, age in friend_ages.items():
  age += 1
  print(f"{name} is now {age}")

# Add two new colours to your list of favourite colours.
fav_colours.append('yellow')
fav_colours.append('emerald')
print(fav_colours)



# ---------- EXERCISE SIX ---------

# Make a new dictionary that contains a list of movies for each year. Each list of movies should be a list. Below is some data you can use.
movies_by_year = {
  1999 : ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
  2009 : ['Avatar', 'Star Trek', 'District 9'],
  2019 : ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}

# Make a new list that contains each row of the buttons on a phone. Each row should be a list.
phone_buttons = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  ["*", 0, '#']
]

# Make a new list that contains information about three countries. Each country should be a dictionary that has a name, a continent, and whether or not it is an island.
countries = [
  {'name': 'Canada', 'continent': 'North America', 'island': False},
  {'name': 'France', 'continent': 'Europe', 'island': False},
  {'name': 'New Zealand', 'continent': 'Oceania', 'island': True}
]

# ---------- EXERCISE SEVEN ---------

# Output the message "I will not skateboard in the halls" 20 times.
for i in range(20):
  print("I will not skateboard in the halls")

# Create a list consisting of the above message. It should appear in the list 20 times.
lines = []

for i in range(20):
  lines.append('I will not skateboard in the halls')

print(lines)
print(len(lines))

# Create a list consisting of the numbers between 1 and 50.

number_list = []

for i in range(50):
  number = len(number_list) + 1
  number_list.append(number)

print(number_list)

# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.
not_island_countries = []

for country in countries:
  if country['island'] == False:
    not_island_countries.append(country)

print(not_island_countries)



# ---------- EXERCISE EIGHT ---------
# You want to add up your expenses for the year. Create a list of numbers 
def calc_expense(expenses):
  return sum(expenses)

expenses2018 = [25.76, 50.00, 12.35, 6.25]
expenses2019 = [56.76, 78.10, 2.25]

print("${:.2f}".format(calc_expense(expenses2018)))
print("${:.2f}".format(calc_expense(expenses2019)))
