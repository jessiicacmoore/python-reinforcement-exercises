ordinals = []


def return_ordinal(num):
    if 4 <= num <= 20:
        suffix = "th"
    elif num == 1 or (num % 10) == 1:
        suffix = "st"
    elif num == 2 or (num % 10) == 2:
        suffix = "nd"
    elif num == 3 or (num % 10) == 3:
        suffix = "rd"
    ordinals.append(str(num) + suffix)


for num in range(1, 21):
    return_ordinal(num)

print(ordinals)

# ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th']
