#Write a Python file that asks for three numbers and outputs the largest and smallest.
print("Write integers:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
max = max(a, b, c)
min = min(a, b, c)
print(f"Biggest: {max}")
print(f"Smallest: {min}")