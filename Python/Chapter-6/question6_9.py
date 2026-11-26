# 9. Create a list 
# words = ["Practice", "makes", "a", "man", "perfect"]. 
# Using join(), print the sentence with spaces, then with "-" between the words, 
# and then with no space at all.

words = ["Practice", "makes", "a", "man", "perfect"]

with_spaces = " ".join(words)
with_hyphen = "-".join(words)
no_space = "".join(words)

print(with_spaces)
print(with_hyphen)
print(no_space)