# total taxes to be paid
taxable_income = float(input("Enter your total income this year: "))
tup = (
    (578125-231250) * 0.35, # top contained 35% bracket total
    (231250-182100) * 0.32, # contained 32% bracket total
    (182100-95375) * 0.24,  # contained 24% bracket total
    (95375-44725) * 0.22,   # contained 22% bracket total
    (44725-11000) * 0.12,   # contained 12% bracket total
    11000 * 0.10            # bottom 10% bracket total
)

# 37% bracket
if taxable_income >= 578126:
    total_tax = (taxable_income - 578125) * 0.37 + sum(tup[0:])
# 35% bracket
elif taxable_income >= 231251:
    total_tax = (taxable_income - 231250) * 0.35 + sum(tup[1:])
# 32% bracket
elif taxable_income >= 182101:
    total_tax = (taxable_income - 182100) * 0.32 + sum(tup[2:])
# 24% bracket
elif taxable_income >= 95376:
    total_tax = (taxable_income - 95375) * 0.24 + sum(tup[3:])
# 22% bracket
elif taxable_income >= 44726:
    total_tax = (taxable_income - 44725) * 0.22 + sum(tup[4:])
# 12% bracket
elif taxable_income >= 11001:
    total_tax = (taxable_income - 11000) * 0.12 + sum(tup[5:])
# 10% bracket
else:
    total_tax = taxable_income * 0.10

print(f"You owe ${total_tax:.2f} this year.")