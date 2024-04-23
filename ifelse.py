height = int(input("What Is Your Height In Cm ? "))
age = int(input("What Is Your Age "))
photo = input("Are You Wanna Take A Photo ? ")
bill = 0

if height >= 120 :
    print("You Can Play Rollercoaster")
    if age <= 12 :
        bill += 5
    elif age <= 18 :
        bill += 7
    elif age >= 45 and age <= 55 :
        print("You Cannot Have To Pay To Play Rollercoaster")
    else : 
        bill += 12
else :
    print("Sorry, You Can't Play Rollercoaster")

if photo == "yes" :
    bill += 3
else :
    bill += 0

print(f"Your Total Bill Is : ${bill}")
