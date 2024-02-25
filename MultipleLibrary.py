class multipleFunctions():
    def OddEven():
        num=int(input("Enter a Number"))
        if(num%2==0):
            print(num,"is Even Number")
            message="Even Number"
        else:
            print(num,"is Odd Number")
            message="Odd Number"
            return message
        
    def ElegibilityForMarriage():
        gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(gender=="Male"and Age<21):
            print("NOT ELIGIBLE")
            status=('Not Eligible')
        elif(gender=="Female"and Age<18):
            print("NOT ELIGIBLE")
            status=('Not Eligible')
            return status 
        
    def percentage():
        sub1=int(input("Subject 1="))
        sub2=int(input("Subject 2="))
        sub3=int(input("Subject 3="))
        sub4=int(input("Subject 4="))
        sub5=int(input("Subject 5="))
        add=sub1+sub2+sub3+sub4+sub5
        percentage=(add)*100/(5*100)
        print("Total:",add)
        percent="add"
        print("Percentage:",percentage)
        percent="percentage"
        return percent
    
    def areaOfTriangle():
        Side1=int(input("Height:"))
        Side2=int(input("Breadth:"))
        Area=(Side1*Side2)/2
        print("Area of Triangle:",Area)
        return Area
    
    def perimeterOfTriangle():
        Side1=int(input("Height:"))
        Side2=int(input("Breadth:"))
        Side3=int(input("Length:"))
        Perimeter=Side1+Side2+Side3
        print("Perimeter of Triangle:",Perimeter)
        return Perimeter
    
    def subfields():
        lists='Machine Learning','Neural Network','Vision','Robotics','Speech Processiong','Natural Language Processing'
        print("Subfields in AI are:")
        for AI in lists:
            print(AI)
            AI=lists
        return AI
    