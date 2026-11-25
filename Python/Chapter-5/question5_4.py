# 4. Write a program that asks the user to enter a 6-digit PIN code. 
# Using isdigit() and len(), print "Valid PIN code" 
# only if it contains only digits and has exactly 6 characters.

pincode = input("Enter your 6 digit pin code: ")

if pincode.isdigit() and len(pincode) == 6:
    print("Valid PIN code")
else:
    print("Invalid PIN Code. It must contain only digits")