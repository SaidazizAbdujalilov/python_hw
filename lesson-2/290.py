#Write a program that asks the user for a sentence and prints the number of words in it.
A = input("Write something: ")
B = A.strip()
C = ''.join(char for char in B if char in " ")
D = len(C)+1
print(f"there are {D} words in your sentence")