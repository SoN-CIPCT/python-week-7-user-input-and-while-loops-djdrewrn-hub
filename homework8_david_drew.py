# list for pizza_orders
pizza_orders = ["pepperoni", "cheese", "combo"]

# list for finished_pizzas
finished_pizzas = []

# loop through pizza orders
while pizza_orders:
    pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    
# Move the pizza to finished_pizzas
    finished_pizzas.append(pizza)

# Print a message for each finished pizza
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
