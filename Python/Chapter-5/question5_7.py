# 7. Create a string password = "secret123". 
# Using islower() and isupper(), 
# print whether the password is fully lowercase, 
# fully uppercase, or mixed case.

password = "secret123"

if password.islower():
    print("Password is fully in lowercase")
elif password.isupper():
    print("Passwrod is fully in uppercase")
else:
    print("Password is in mixed case")