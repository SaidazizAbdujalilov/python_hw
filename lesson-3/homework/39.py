#Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
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
        D = int(input("Type the number of elements in your sublists: "))
        for i in range(0, len(B), D):
            C.append(B[i:i+D])
        print(C)
