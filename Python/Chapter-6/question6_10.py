# 10. Create a string sentence = "learning python is fun and useful". 
# Using split(), title() and join(), convert it into 
# "Learning-Python-Is-Fun-And-Useful" and print the result.

sentence = "learning python is fun and useful"

words = sentence.split()
title_words = [word.title() for word in words]
result = "-".join(title_words)

print(result)