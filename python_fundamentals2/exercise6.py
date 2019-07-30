def temperature_converter(f):
  c = (f-32)*5/9

  print(f"{f} degrees fahrenheit is {c} degrees celsius!")

print("Enter a temperature to convert from fahrenheit to celsius:")
f = int(input())

temperature_converter(f)