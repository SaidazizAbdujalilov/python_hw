#Check Element: Given a tuple and an element, check if the element is present in the tuple.
B = []
while True:
    A = (input("Write something from your tuple or write 'stop()' to finish the tuple: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)

if len(B) == 0:
    print("your tuple is empty")
else:
    if len(max(B)) == 0:
        print("your tuple is empty")
    else:
        C = tuple(B)
        print(f"""Here is your tuple: 
              {C}""")
        D = input("Enter the element to check: ").strip()
        print(bool(D in C))