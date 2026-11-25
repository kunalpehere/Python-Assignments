# 8. Create a list scores = [45, 60, 75]. 
# Print its id(), change the second value to 65, and print the list and its id() again. 
# Do the same with a string variable, by assigning a new value to it. 
# Write a comment comparing the id() results.

scores = [45, 60, 75]
print("Initial scores:", scores, "| id:", id(scores))

scores[1] = 65
print("Updated scores:", scores, "| id:", id(scores))

greeting = "Hello"
print("Initial greeting:", greeting, "| id:", id(greeting))

greeting = "Hello World"
print("Updated greeting:", greeting, "| id:", id(greeting))
