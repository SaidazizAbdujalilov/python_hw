#Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
A = int(input("Type the first number: "))
B = int(input("Type the last number: "))
C = []
while A<=B:
    C.append(A)
    A = A + 1
print(C)

A = int(input("Type the first number: "))
D = list(range(A,B+1))
print(D)