#Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
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
        for item in B:
            if item not in C:
                C.append(item)
        print(C)