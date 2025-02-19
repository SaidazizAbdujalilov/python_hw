#Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
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
            if int(item) % 2 - 1 == 0:
                C.append(item)
        print(f"there is the list of odd numbers: {C}")