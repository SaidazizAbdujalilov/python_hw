#Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

D = int(input("Enter the index of starting item of your sublist: "))
E = int(input("Enter the index of ending item of your sublist: "))
C = B[D-1:E+1]
print(f"Here is your sublist: {C}")
if len(B) == 0:
    print("your list is empty")
else:
    if len(max(B)) == 0:
        print("your list is empty")
    else:
        print(f"The maximum item in your sublist is '{max(C)}'")