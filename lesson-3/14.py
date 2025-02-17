#Check for Empty List: Determine if a list is empty and return a boolean.
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

if len(B) == 0:
    print(bool(0))
else:
    if len(max(B)):
        print(bool(0))
    else:
        print(bool(0))