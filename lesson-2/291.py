#Write a program to check if a string contains any digits.
A = input("Write something: ")
B = ''.join(char for char in A if char in "012345789")
if len(B)>0: 
    print("Your input has digit")
else:
    print("Your input has no digit")