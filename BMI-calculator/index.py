def bmi():
    name = input("My name is ")
    height_m = float(input("My height in metres is "))
    weight_kg = float(input("My weight in kg is "))
    bmi = weight_kg/height_m**2
    if bmi < 25 and bmi >=18.5:
        print("bmi is" + " " + str(bmi))
        print(name + " " + "is healthy")
    elif bmi < 18.5:
        print("bmi is" + " " + str(bmi))
        print(name + " " + "is underweight")
    elif bmi >=25 and bmi <29.9:
        print("bmi is" + " " + str(bmi))
        print(name + " " + "is overweight")
    elif bmi >= 30:
        print("bmi is" + " " + str(bmi))
        print(name + " " + "is Obese")