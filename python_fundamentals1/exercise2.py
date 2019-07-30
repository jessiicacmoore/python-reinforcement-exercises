# ------ Calculating Tip -----

# Print meal amount
print("The meal is 55 dollars.") 

# calculate 15% of meal amount and make integer with string interpolation
# print("I will tip {} dollars!".format(int(55*.15)))

# This will not work - can only concatenate strings
# print("I will tip " + (55*.15)) 

# Converting number to string
print("I will tip: " + str(55*.15) + " dollars!")

# Wanted to see if you could convert to integer and then string, but did not work
# print("I will tip " str(int(55*.15)) + " dollars!")


# ------ String Interpolation -----
 
print("What is the result of 45828 multiplied by 7839?\nThe answer is {}!".format(45628*7839))


# ------ Expression question -----

print("The value of the expression (10 < 20 and 30 < 20) or not(10 == 11) is {}.".format((10 < 20 and 30 < 20) or not(10 == 11)))