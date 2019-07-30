digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
en = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
fr = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
esp = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]


dict = {}


def make_dict():
    for digit in digits:
        i = digits.index(digit)
        dict.update({digit: {"french": fr[i], "spanish": esp[i], "english": en[i]}})


make_dict()
print(dict)

# {
#     "1": {"french": "un", "spanish": "uno", "english": "one"},
#     "2": {"french": "deux", "spanish": "dos", "english": "two"},
#     "3": {"french": "trois", "spanish": "tres", "english": "three"},
#     "4": {"french": "quatre", "spanish": "cuatro", "english": "four"},
#     "5": {"french": "cinq", "spanish": "cinco", "english": "five"},
#     "6": {"french": "six", "spanish": "seis", "english": "six"},
#     "7": {"french": "sept", "spanish": "siete", "english": "seven"},
#     "8": {"french": "huit", "spanish": "ocho", "english": "eight"},
#     "9": {"french": "neuf", "spanish": "nueve", "english": "nine"},
# }


# def make_dict():
#     i = 0

#     for digit in digits:
#         dict.update({digits[i]: {"french": fr[i], "spanish": esp[i], "english": en[i]}})
#         i += 1
