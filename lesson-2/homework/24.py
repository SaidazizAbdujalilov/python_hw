#Write a Python program to check if a given string is palindrome or not.
A = input("Write something: ")
B = A[::-1]
if A == B: print(f"{A} is a polindrome")
else: 
    print(f"{A} is not a polindrome")
