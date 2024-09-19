def cal_sum (num1 , num2):
    return num1 + num2
def cal_multiplication (num1 , num2):
    return num1 * num2
def cal_subtraction (num1 , num2):
    return num1 - num2
def cal_division (num1 , num2):
    if num2 == 0:
        return "can not divide by zero."
    else:
        return num1 / num2
num1 = int(input("Enter 1st number: "))
operation = input ("Enter your desired operation i.e, + , _ , * , / : ")
num2 = int(input("Enter 2nd number: "))
if operation == '+' :
    print (f"{num1} + {num2} = {cal_sum(num1,num2)}")
if operation == '-' :
    print (f"{num1} - {num2} = {cal_subtraction(num1,num2)}")
if operation == '*' :
    print (f"{num1} * {num2} = {cal_multiplication(num1,num2)}")
if operation == '/' :
    print (f"{num1} / {num2} = {cal_division(num1,num2)}")