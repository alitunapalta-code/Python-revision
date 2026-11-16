field1 = 140
field2 = 30
field3 = 20
field4 = 220
field5 = 170

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest: ", total, "kg")
print("Average per field", average, "kg")

price_per_kg = 5
earnings = total * price_per_kg
print("Total earnings: ",earnings,"euros")

bags = total//25
leftover = total%25

print("full bags packed: ",bags)
print("Leftover grain: ",leftover)

last_year = 250
print("Better than last year?", total > last_year)
print("Same as last year?", total == last_year)
print("As good as last year?", total >= last_year)

total += 40
print("After bonus crop: ",total, "kg")

total -= 25
print("After seed reserve: ",total, "kg")

bags = total // 25
print("Final bags packed: ",bags)