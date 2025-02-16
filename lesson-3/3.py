#Max Element: From a given list, determine the largest element.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

C = ""
D = "."
for word in B:
    if len(C) <= len(word):
        C = word
if len(C) < len(D):
        print("Your list is empty")
print(C)

#other one

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
    print(max(B))