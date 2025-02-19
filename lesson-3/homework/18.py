#Find Sublist: Given a list and a sublist, check if the sublist exists within the list.
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)

C = []
while True:
    D = (input("Write something from your sublist or write 'stop()' to finish the list: ")).strip()
    if D.lower() == "stop()":
        break
    C.append(D)
print(f"""Here is your list:
{B}""")
print(f"""Here is your sublist:
{C}""")

if len(B) == 0:
    print("your list is empty")
else:
    if len(max(B)) == 0:
        print("your list is empty")
    else:
        if len(C) == 0:
            print("your sublist is empty")
        else:
            if len(max(C)) == 0:
                print("your sublist is empty")
            else:
                if all(item in B for item in C):
                    print("Your list contains your sublist")
                else:
                    print("Your list does not contain your sublist")