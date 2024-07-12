w=float(input("Input your weight : "))
h=float(input("Input your height : "))
bmi=float(w//h**2)
print("Your BMI = {}".format(bmi))
if bmi < 16:
    print("Your classification is Servere Thinness")
elif 16 >= bmi < 17:
    print("Your classification is Moderate Thinness")
elif 17 >= bmi < 18.5:
    print("Your classification is Mild Thinness")
elif 18.5 >= bmi < 25:
    print("Your classification is Normal")
elif 25 > bmi <= 30:
    print("Your classification is Overweight")
elif 30 > bmi <= 35:
    print("Your classification is Obese Class I")
elif 35 > bmi <= 40:
    print("Your classification is Obese Class II")
else:
    print("Your classification is Obese Class III")
