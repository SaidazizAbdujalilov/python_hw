#Write a Python program to check if one string contains another.
A = input("Write something: ")
B = input("Write something: ")
if B in A:
    print(f"{A} contains {B}")
else:
    if A in B:
        print(f"{B} contains {A}")
    else:
        print("strings are not interconnected")
        