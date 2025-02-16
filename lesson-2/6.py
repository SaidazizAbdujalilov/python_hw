#Create a program that accepts a number and returns the last digit of that number.
A = input("Number: ")
if A.isdigit(): 
    B = A[len(A)-1]
    print(f"Last digit: {B}")
else: 
    A = input("Number: ")
    if A.isdigit(): 
       B = A[len(A)-1]
       print(f"Last digit: {B}")
    else: 
        print("Go to hell")
