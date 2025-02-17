#Index of Element: Given a list and an element, find the index of the first occurrence of the element.
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
    C = input("Write the element you want to find from the list: ")
    D = B.index(C) +1 
    print(f"your element is {D}th")
