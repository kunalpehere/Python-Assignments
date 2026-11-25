# 2. Create a string fruit = "watermelon", 
# print the 3rd character from the end using negative indexing. 
# Then try to print fruit[-15] and write a comment about the error you get.

fruit = "watermelon"

print("3rd character from the end using negative indexing", fruit[-3]) # ouput -> l
print(fruit[-15]) # Output -> IndexError: string index out of range