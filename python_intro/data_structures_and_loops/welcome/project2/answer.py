# Make Some Pizzas

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'achovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

pizzas = list(zip(toppings, prices))
print(pizzas)

# Sorting and Slicing Pizzas

pizzas.sort(key = lambda x : x[1])

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
