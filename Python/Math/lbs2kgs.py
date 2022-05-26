weight = input("Enter your weight: ")
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "L":
    newWeight = float(weight) * 0.45
    print("Weight in Kg: " + str(newWeight))
else:
    newWeight = float(weight) / 0.45
    print("Weight in Lbs: " + str(newWeight))