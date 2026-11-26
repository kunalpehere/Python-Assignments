# 3. Create a string email = "kiran.joshi@yahoo.com". 
# Using partition("@"), 
# separate the username and the domain, and print both.

email = "kiran.joshi@yahoo.com"

separate = email.partition("@")

print("Username:", separate[0])
print("Domain:", separate[2])