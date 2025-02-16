#Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

C = []

if len(max(B)) == 0:
    print("your list is empty")
else:
    for word in B:
        if word not in C:
            C.append(word)
print(f"""Here is the shortened version of your list:
{C}""")