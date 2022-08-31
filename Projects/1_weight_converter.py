from tkinter import Scale


weight = float(input("Weight: "))

scale = input("(L)bs or (K)g: ")

if scale.upper() == "L":
    kg = weight * 0.4536
    print(f"You are {kg} kilograms")
elif scale.upper() == "K":
    lbs = weight * 2.20
    print(f"You are {lbs} pounds")
else:
    print("there is no such option")
