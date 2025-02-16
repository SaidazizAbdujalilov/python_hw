#Sum of Elements: Given a list of numbers, calculate the total of all the elements.
B = []
while True:
    A = float(input("Type something from your list of numbers or type '0' to finish the list: "))
    if A == 0:
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

print(sum(B))