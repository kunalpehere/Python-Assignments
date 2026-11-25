# 3. Write a program that asks the user to enter their first name. 
# Using isalpha(), print "Valid name" if it contains only letters, 
# otherwise print "Name should contain only letters".

first_name = input("Enter your first name: ")

if first_name.isalpha():
    print("Valid name")
else:
    print("Name should contain only letters")