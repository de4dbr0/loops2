weight= input("enter your weight(kg): ")
height= input("enter your height(cm): ")
height2= int(height)/100
bmi=int(weight)/(float(height2)*float(height2))
print("your bmi is:",bmi)
if bmi<=18.4:
    print("you are underweight")
elif bmi>18.4 and bmi<=24.9:
    print("you are normal")
elif bmi>24.9 and bmi<39.9:
    print("you are overweight")
elif bmi>39.9:
    print("you are obese")
