# mini activity 3

# price cents

price_cents = int(input("Enter the price of the item in cents: "))
tax_rate_percent = int(input(" Enter thr tax rate( as whole number, e.g. 13 for 13%): "))

# calculating tax and total in cents
tax_cents = price_cents 
tax_rate_percent // 100
total_cents = price_cents + tax_cents

# convert into dollars
price = price_cents / 100
tax = tax_cents / 100
total = total_cents / 100

# printing

print(f"price: ${price:.2f}")
print(f"tax: ${tax:.2f}")
print(f"total: ${total:.2f}")
