#Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
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
        for item in B:
            if int(item) <= 0:
                C.append(int(item))
        print(sum(C))