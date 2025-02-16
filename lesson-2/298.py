#Write a program that checks if a string starts with one word and ends with another.
#Example:
#Input: "Python is fun!"
#Starts with: "Python"
#Ends with: "fun!"
A = input("Write something: ")
B = A.split()
C = B[0]
D = B[-1]
print(f"""First word: {C} 
Last word: {D}""")