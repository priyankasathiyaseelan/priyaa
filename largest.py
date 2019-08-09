num1=int(input("Enter the first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter the third number: "))
#get input from user for num1,num2,num3
if(num1>num2) and (num1>num3):
    biggest=num1;
#check whether the num1 is smaller than num2 and num3
elif (num2>num1) and (num2>num3):
    biggest=num2;
#check whether the num2 is smaller than num1 and num3
else:
    biggest=num3;
print("The largest number is",biggest);
