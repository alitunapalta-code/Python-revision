tempurature = int(input("Enter the tempurature in dgerees celcius: "))

if tempurature < 20:
    outfit = "jacket"
    print("it is cold today.")
    print("wear a", outfit)
else:
    outfit = "T-shirt"
    print("it is warm today.")
    print("Wear a", outfit)

is_raining = input("Is it raining today? (yes/no)")

if is_raining == "yes":
    print("Bring an umbrella")

wind_speed = int(input("enter the wind speed in km/h: "))

if wind_speed > 30:
    windbreaker = "yes"
    print("it is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    windbreaker = "no"
    print("The weather is calm")
    print("No windbreaker needed over your", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no)")

if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
if has_puddles == "no":
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

print("")
print("Weather Check Complete!")

print("=====WEATHER OUTFIT PICKER======")
print("Tempurature: ", tempurature)
print("Outfit chosen: ", outfit)
print("Raining: ", is_raining)
print("Windbreaker needed: ", windbreaker)
print("Shoes chosen: ", shoes)
print("================================")