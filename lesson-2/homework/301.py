#Write a program that accepts a username and password and checks if both are not empty.
A = bool(input("Write your username: "))
B = bool(input("Write your password: "))
if A == True:
    C = "valid"
else:
    C = "empty"

if B == True:
    D = "valid"
else:
    D = "empty"
print(f"Your username is {C} and password is {D}")