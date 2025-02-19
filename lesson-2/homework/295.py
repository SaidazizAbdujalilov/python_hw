#Ask the user for a sentence and create an acronym from the first letters of each word.
#Example:

#Input: "World Health Organization"
#Output: "WHO"
A = input("Write your company name: ")
B = A.split()
C = ''.join(word[0].upper() for word in B)
print(C)
