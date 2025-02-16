#Write a program that checks if a number is positive and even.
A = int(input("Write and integer: "))
if A > 0:
    B = "positive"
else:
    B = "negative"
D = str(A)
if D[-1] in "24680":
    C = "even"
else:
    C = "odd"
print(f"Your number is {B} and {C}")
