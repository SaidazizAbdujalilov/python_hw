#Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
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
        D=int(input("Write the number of times you want the elements to repeat: "))
        C=[item for item in B for _ in range(D)]
        print(C)