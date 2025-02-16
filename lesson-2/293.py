#Ask the user for a string and remove all spaces from it.
A = input("Write something: ")
B = ''.join(char for char in A if char not in " ")
print(B)