def sum_odd_numbers(number_list):
  odd_numbers = []
  for number in number_list:
    if number % 2 != 0:
      odd_numbers.append(number)
  return sum(odd_numbers)

print (sum_odd_numbers([1,2,3,4,5,6,7,8,9,10]))