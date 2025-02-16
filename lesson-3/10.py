#Sort List: Create a new list that contains the elements of the original list in sorted order.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

if len(max(B)) == 0:
    print("your list is empty")
else:
    print(sorted(B))