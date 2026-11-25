# 8. Create a string sentence = "I like tea, my friend likes tea, and my mother also likes tea". 
# Using find(), print the position of the first occurrence of "tea" and the position of "coffee". 
# Write a comment explaining the result for "coffee".

sentence = "I like tea, my friend likes tea, and my mother also likes tea"

print(sentence.find("tea"))
print(sentence.find("coffee"))

# Explanation for "coffee"
# str.find() returns the starting index of the first match, 
# or -1 if the substring is not found.
# Since "coffee" does not appear anywhere in 'sentence', it return -1


