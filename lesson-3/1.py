#Count Occurrences: Given a list and an element, find how many times the element appears in the list.

B = []
while True:
    A = (input("Write something from your list or write 'stop()' to finish the list: ")).strip()
    if A.lower() == "stop()":
        break
    B.append(A)
print(f"""Here is your list:
{B}""")

C = input("Enter an item to be counted in your list: ")
D = 0
for word in B:
    if word == C:
     D += 1
print(f"The number of '{C}'s in your list is {D}")