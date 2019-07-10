number_of_pizzas = eval(input("How many pizzas do you want?") )
cost_per_pizza = eval(input("How much does the pizza cost?") )
subtotal = number_of_pizzas * cost_per_pizza
tax_rate = 0.04
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sales tax.")
