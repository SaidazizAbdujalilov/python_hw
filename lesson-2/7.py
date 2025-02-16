#Create a program that takes a number and checks if it’s even or not.
A = input("Enter the integer:")
if A[len(A)-1] in "02468":
    print(f"{A} is even")
else:
    print(f"{A} is odd")