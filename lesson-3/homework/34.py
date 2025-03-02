#Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
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
        D = int(input("type the number movements you want to do in rotation: "))
        C = B[-D:]+B[:-D]
        print(C)