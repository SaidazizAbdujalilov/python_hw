#Find All Indices: Given a list and an element, find all the indices of that element in the list.
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

C = []

if len(B) == 0:
    print("your list is empty")
else:
    if len(max(B)) == 0:
        print("your list is empty")
    else:
        D = input("Write the item you want find: ").strip()
        for item in B:
            E = B.index(item) +1
            if item == D:
                C.append(E)
            E = E -1
            B[E] = " "
        print(C)