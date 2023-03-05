import math

print('''Welcome to the KB_Tech Calculator:
Following are the operations you can do it with the help of this Calculator. Please select accordingly.
1. Addition.
2. Substraction.
3. Multiplication.
4. Division.
5. Exponent.
6. Sqaure Root.
''')

Select_Op= int(input("Please select the operation you want to perform: \n"))
Name= "Komail"
Password= "123"

if Select_Op==1:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Number one: \n"))
        Number_2= float(input("Please Enter Number two: \n"))
        Result= Number_1 + Number_2
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")
        
elif Select_Op==2:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Number one: \n"))
        Number_2= float(input("Please Enter Number two: \n"))
        Result= Number_1 - Number_2
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")

elif Select_Op==3:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Number one: \n"))
        Number_2= float(input("Please Enter Number two: \n"))
        Result= Number_1 * Number_2
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")

elif Select_Op==4:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Number one: \n"))
        Number_2= float(input("Please Enter Number two: \n"))
        Result= Number_1 / Number_2
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")

elif Select_Op==5:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Base Number : \n"))
        Number_2= float(input("Please Enter Power you want to calculate: \n"))
        Result= (Number_1)**Number_2
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")

elif Select_Op==6:
    print("Please Verify Your Credentials before using this Calculator:")
    Entered_Name= str(input("Please Enter Your Name: \n"))
    Entered_Password= str(input("Please Enter Your Password: \n"))
    if Entered_Name==Name and Entered_Password==Password:
        print("You are verified: \n")
        Number_1= float(input("Please Enter Number: \n"))
        Result= (Number_1)**0.5
        print("Result is : ", Result)
    else:
        print("You are not eligible to use this Calculator: \n")

else:
    print("You have entered invalid option: ")
    


