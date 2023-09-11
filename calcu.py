class Calculation():
    def Elegible():
        gender=input("Your Gender:(Male/Female):")
        age=int(input("Your Age:"))
        if (gender=="Male"):
            if(age>=21):
                print("Elegible")
            else:
                print("Not Elegible")
        elif (gender=="Female"):
            if(age>18):
                print("Elegible")
            else:
                print("Not Elegible")
        else:
            print("Invalid input")  
            
    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area Formula:(Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Base=int (input("Base:"))
        Peri=Height1+Height2+Base
        print ("Perimeter formula:Height1+Height2+Base")
        print ("Perimeter of Triangle:",Peri)
     
    def Percentage():
        m1=int (input("Subject1="))
        m2=int (input("Subject2="))
        m3=int (input("Subject3="))
        m4=int (input("Subject4="))
        m5=int (input("Subject5="))
        Total=m1+m2+m3+m4+m5
        print("Total:",Total)
        Percent=(Total/500)*100
        print("Percentage:",Percent)