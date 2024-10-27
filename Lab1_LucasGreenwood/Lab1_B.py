# Part B : calculate the sales tax on a purchased item

# prompt and cast price to a float
price = float(input("Enter the price of the item: "))

# prompt and cast tax to a float
sales_tax_percentage = float(input("Enter the sales tax percentage: "))/100

# calculate tax from the price and sales_tax_percentage
tax = price * sales_tax_percentage
price += tax

# print the calculated total price
print(f"Your total is ${price:.2f}")