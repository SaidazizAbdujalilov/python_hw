#Write a program that counts the number of vowels and consonants in a given string.
A = input("Write something: ") 
B = ''.join(char for char in A if char.lower() in 'euioa')
C = ''.join(char for char in A if char.lower() in 'qwrtypsdfghjklzxcvbnm')
print(f"Vowels: {len(B)}")
print(f"Consonants: {len(C)}")
