#Remove Element by Index: Given a list and an index, remove the element at that index if it exists.'
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
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
        C = int(input("at which position is your item that you want to remove? "))
        if bool(B[C]) == True:
            B.remove(B[C -1])
            print(f"the updated list is: {B}")
        else:
            print(f"There is no item at index of {C}")
