#Replace Element: Given a list, replace the first occurrence of a specified element with another element.
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
        C = input("Write the item you want to add to the list: ").strip()
        D = input("Write the item you want to replace it with: ").strip()
        E = B.index(D)
        B[E] = C
        print(f"Here is the updated list: {B}")