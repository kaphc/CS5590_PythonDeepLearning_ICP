strength = int(input("Enter the number of students : "))

weightLBS = []
weightKGS = []

for student in range(strength):
    weight = float(input("Enter the " + str(student) + " student weight in LBS : "))
    weightLBS.append(weight)
    weight = weight * 0.453592
    weightKGS.append(round(weight, 2))

print("Students weight in LBS")
print(weightLBS)
print("Students weight in KGS")
print(weightKGS)
