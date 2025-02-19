#Insert Element: Given a list and an element, insert the element at a specified index.
B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

if len(B) == 0:
    print("your list is empty")
else: 
    if len(max(B)) == 0:
        print("your list is empty")
    else:
       C = input("Write the thing that you want to insert: ")
       D = input(f""""{C}" should come after (write "idk" if you do not know): """).strip()
       if D.lower() == "idk":
          E = int(input(f""""{C}" shall come at which position? Write an integer: """)) - 1
          B.insert(E,C)
          print(B)
       else: 
          F = B.index(D) + 1
          B.insert(F,C)
          print(B)
