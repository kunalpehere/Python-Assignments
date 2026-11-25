# 7. Create a string language = "java". 
# Try to change the first letter to "J" using language[0] = "J" and write a comment about the error. 
# Then create a new string "Java" using concatenation and slicing (without typing the whole word again).

Language = "java"

# Language[0] = "J"


print(Language) # Output -> TypeError: 'str' object does not support item assignment

new_language = "J" + Language[1:]

print(new_language)