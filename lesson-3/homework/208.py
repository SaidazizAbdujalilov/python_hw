#Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
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
        D = B[0:3]
        E = tuple(D)
        print(E)