money = int(input("Please enter money: "))
# Compute the number of quarters
quarters = money // 25
# Compute left over money
money = money % 25
#Compute the number of dimes
dimes = money // 10
# Compute left over money
money = money % 10
#Compute the number of nickels
nickels = money // 5
# Compute left over money
pennies = money % 5

# Print results
print('quarters:', quarters)
print('dimes:', dimes)
print('nickels:', nickels)
print('pennies:', pennies)
