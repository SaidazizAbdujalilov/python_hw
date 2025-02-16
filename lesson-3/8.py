#Slice List: Create a new list that contains only the first three elements of the original list.

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
    if len(B) >= 3:
        C = [B[0],B[1],B[2]]
    else:
        print("Your list has less than 3 items")
print(f"""Here are the first 3 items in your list:
{C}""")