#Sum of Elements: Given a list of numbers, calculate the total of all the elements.
B = []
while True:
    A = float(input("Type something from your list of numbers or type '0' to finish the list: "))
    if A == 0:
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

if len(B) == 0:
    print("your list is empty")
else: 
    if len(max(B)) == 0:
     print("your list is empty")
    else:
     print(sum(B))