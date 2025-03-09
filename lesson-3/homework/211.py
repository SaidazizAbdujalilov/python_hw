#Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
B = []
while True:
    A = (input("Write something from your tuple or write 'stop()' to finish the tuple: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
E=[]
if len(B) == 0:
    print("your tuple is empty")
else:
    if len(max(B)) == 0:
        print("your tuple is empty")
    else:
        C = tuple(B)
        print(f"""Here is your tuple: 
              {C}""")
        D = input("Type the element to check: ")
        for item in C:
            E = [index for index, item in enumerate(C) if item == D]
        print(E)