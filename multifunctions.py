class  multipleFunctions():
    def oddEven():
        num=int(input("Enter the number:"))
        if ((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
        return message
    
    def BMI():    
        weight=float(input("Enter Your Weight in kg:"))
        height=float(input("Enter Your Height in cm:"))
        bmi= weight/(height/100)**2
        print(f"Your BMI is {bmi}")
        if bmi<=18.4:
            print ("Underweight")
            message="underweight"
        elif bmi<=24.9:
            print ("Normal Range")
            message="Normal Range"
        elif bmi<=29.9:
            print("Overweight")
            message="Overweight"
        elif bmi<=30:
            print("Obese")
            message="Obese"
        elif bmi<=34.9:
            print("Obese I")
            message="Obese I"
        elif bmi<=39.9:
            print ("Obese II")
            message="Obese II"
        else:
            print("Obese III")
            message="Obese III"
        return message
    
            