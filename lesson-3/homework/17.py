#Concatenate Lists: Given two lists, create a new list that combines both lists.
B = []
while True:
    A = (input("Write something from your list number 1 or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)

C = []
while True:
    D = (input("Write something from your list number 2 or write 'stop()' to finish the list: ")).strip()
    if D.lower() == "stop()":
        break
    C.append(D)
print(f"""Here is your number 1 list:
{B}""")
print(f"""Here is your number 2 list:
{C}""")

E = []

if len(B) == 0:
    print("your list number 1 is empty")
else:
    if len(max(B)) == 0:
        print("your list number 1 is empty")
    else:
        for char in (B):
            E.append(char)

if len(C) == 0:
    print("your list number 2 is empty")
else:
    if len(max(C)) == 0:
        print("your list number 2 is empty")
    else:
        for char in (C):
            E.append(char)
        print(f"There is the list containing your both lists {E}")