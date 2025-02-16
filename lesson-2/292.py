#Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).
B = []
while True:
    A = input("Write one item in your list or write 'stop' to close the list: ")
    if A.lower() == "stop": 
        break
    B.append(A)
C = "{>_<*}".join(B)
print(C)