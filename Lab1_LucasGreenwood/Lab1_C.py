# Part C : calculate the number of days between 2 dates.

# prompt and typecast inputs
year1 = int(input("Enter the year for date 1: "))
month1 = int(input("Enter the month for date 1: "))
day1 = int(input("Enter the day for date 1: "))

year2 = int(input("Enter the year for date 2: "))
month2 = int(input("Enter the month for date 2: "))
day2 = int(input("Enter the day for date 2: "))

# calculate difference in the dates : first convert to days
difference = abs((year2 * 360 + month2 * 30 + day2) - (year1 * 360 + month1 * 30 + day1))

# display results
print(f"The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {difference} days!")