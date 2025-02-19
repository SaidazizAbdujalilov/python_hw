#Write a program that takes three numbers and checks if all of them are different.
A = float(input("Write a number: "))
B = float(input("Write a number: "))
C = float(input("Write a number: "))
if A/B > B/A:
    D = bool(0)
else:
    D = bool(1)
if A/C > C/D:
    E = bool(0)
else:
    E = bool(1)
if B/C > C/B:
    F = bool(0)
else:
    F = bool(1)
if D == E == F == True:
    print("Your numbers are the same")
else:
    print("Your numbers are not the same")
