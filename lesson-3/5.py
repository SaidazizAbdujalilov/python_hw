#Check Element: Given a list and an element, check if the element is present in the list.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

C = input("Which item's presence would you like to check? ")
if C in B:
    print(f"Yes, {C} is present in your list")
else:
    print(f"No, {C} is not present in your list")