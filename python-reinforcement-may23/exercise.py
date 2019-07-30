# Define a function called word_counter that accepts one string argument and returns a number representing how many separate words are in that string. For example:

def word_counter(string_input):
    print(len(string_input.split()))


word_counter("Hello world") # returns 2

word_counter("This is a sentence") # returns 4

word_counter("") # returns 0

word_counter("What do you call a thieving alligator? A Crookodile") #9