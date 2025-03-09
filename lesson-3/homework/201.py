#Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
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
              {B}""")
        D = input("Name the item you want to check: ")
        E = 0
        for item in C:
            if item == D:
                E = E + 1
        print(E)