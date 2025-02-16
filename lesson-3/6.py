#First Element: Access the first element of a list, considering what to return if the list is empty.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

if len(max(B)) == 0:
    print("your list is empty")
else:
    print(B[0])