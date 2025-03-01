#Merge and Sort: Given two lists, create a new sorted list that merges both lists.
B = []
while True:
    A = (input("Write something from your 1st list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your 1st list:
{B}""")

C = []
while True:
    D = (input("Write something from your 2nd list or write 'stop()' to finish the list: ")).strip()
    if D.lower() == "stop()":
        break
    C.append(D)
print(f"""Here is your 2st list:
{C}""")

if len(B) == 0:
    print("your 1st list is empty")
else:
    if len(max(B)) == 0:
        print("your 1st list is empty")
    else:
        if len(C) == 0:
            print("your 2nd list is empty")
        else:
            if len(max(C)) == 0:
                print("your 2nd list is empty")
            else:
                E = B+C
                print(f"Here is your sorted list: {sorted(E)}")