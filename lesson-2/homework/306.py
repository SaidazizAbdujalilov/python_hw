#Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
A = int(input("Write an integer: "))
B = A % 3
C = A % 5
if bool(B)==bool(C)==False:
    print("it is divisible by both 3 and 5")
else:
    print("it is not divisible either by 3 or 5")