#Extract car names from this text: txt = 'LMaasleitbtui'

A = "LMaasleitbtui"
B = ["Tesla", "sui"]
a = A.lower()
b = [word.lower() for word in B]
C = []
for d in b:
    if all(d.count(char) <= a.count(char) for char in d):
        C.append(d)
print(C)
