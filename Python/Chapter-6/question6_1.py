# STRING METHODS – PRACTICE QUESTIONS-SESSION 6

# 1. Create a string skills = "Python Java SQL Excel PowerBI". 
# Using split(), convert it into a list and print the list and 
# the total number of skills using len().

skills = "Python Java SQL Excel PowerBI"

skills_list = skills.split()

print("Before List:", skills)
print("After List:",skills_list)
print("Total number of skills:", len(skills_list))