# ---------- EXERCISE ELEVEN ---------
for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print ('BitMaker')
  elif number % 3 == 0:
    print('Bit')
  elif number % 5 ==0:
    print('Maker')
  else:
    print(number)

# ---------- EXERCISE TWELVE ---------
pizzas = {}
pizza_id = 0

print('How many pizzas do you want to order?')
pizza_qty = int(input())

for pizza in range(pizza_qty):
  pizza_id += 1
  print("How many toppings for Pizza {}".format(pizza_id))
  topping_qty = int(input())

  pizzas['pizza {}'.format(pizza_id)] = topping_qty



print(pizzas)
  
