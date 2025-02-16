#Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
#Example:

#Input sentence: "I love apples."
#Replace: "apples"
#With: "oranges"
#Output: "I love oranges."

A = input("Write your sentence: ")
B = input("Write the word to replace: ")
C = input("Write the word to replace with: ")
D = A.replace(B,C)
print(D)