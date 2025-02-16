#Ask the user for a string and replace all the vowels with a symbol (e.g., *).
A = input('Write something: ')
B = "{>_<*}"
D = ''.join(B if char in "euioaEUIOA"
               else char for char in A)
print(D)