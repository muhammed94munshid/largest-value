num1=float(raw_input("enter first number="))

num2=float(raw_input("enter second number="))

num3=float(raw_input("enter third number="))

if (num1<num2) and (num2<num3):

    print(num3,"is largest")

elif (num1<num3) and (num3<num2):

    print(num2,"is largest")

else:
     print(num1,"is largest")