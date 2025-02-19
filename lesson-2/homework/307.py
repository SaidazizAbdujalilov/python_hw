#Write a program that checks if the sum of two numbers is greater than 50.8. 
#Create a program that checks if a given number is between 10 and 20 (inclusive)
A = float(input("Write any number: "))
B = float(input("Write any number: "))
C = bool(A+B>50.8)
D = bool(10<=A<=20)
E = bool(10<=B<=20)
if C==True:
    if D==True:
        if E==True:
            print("The sum of your numbers, which are between 10 and 20 (inclusive), is greater than 50.8")
        else:
            print(f"The sum of your numbers, {A} is between 10 and 20 (inclusive) and {B} is not, is greater than 50.8")
    else:
        if E==True:
            print(f"The sum of your numbers, {B} is between 10 and 20 (inclusive) and {A} is not, is greater than 50.8")
        else:
            print(f"The sum of your numbers, which are not between 10 and 20 (inclusive), is greater than 50.8")
else:
    if D==True:
        if E==True:
            print("The sum of your numbers, which are between 10 and 20 (inclusive), is not greater than 50.8")
        else:
            print(f"The sum of your numbers, {A} is between 10 and 20 (inclusive) and {B} is not, is not greater than 50.8")
    else:
        if E==True:
            print(f"The sum of your numbers, {B} is between 10 and 20 (inclusive) and {A} is not, is not greater than 50.8")
        else:
            print(f"The sum of your numbers, which are not between 10 and 20 (inclusive), is not greater than 50.8")