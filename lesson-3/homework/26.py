#Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
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
        if len(B) % 2 == 0:
            C = len(B)//2
            D = len(B)//2 - 1
            print(B[C], B[D])
        else:
            E = len(B)//2
            print(B[E])