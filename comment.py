#comment
print("Ali")
print("Swathi")
number = 1000
print(number)

#My program
temp = int(input("Enter the tempurature: "))
if temp < 20:
    print("It is winter")
if temp == 20:
    print("It is spring")
if temp > 20:
    print("It is summer")

#program 2
math_score = int(input("Enter your math grade out of 100% : "))
science_score = int(input("Enter your science grade out of 100% : "))
history_score = int(input("Enter your history grade out of 100% : "))

overall_grade = (math_score + history_score + science_score)
if overall_grade < 150:
    print("You failed")
if overall_grade == 150:
    print("You passed")
if overall_grade > 150:
    print("You got a good grade")