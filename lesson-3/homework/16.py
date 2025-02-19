#Count Odd Numbers: Given a list of integers, count how many of them are odd.
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
        for char in (B):
            if int(char) % 2 - 1 == 0:
                C.append(char)
        print(f"The number of odd characters is: {len(C)}")