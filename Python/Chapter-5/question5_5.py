# 5. Create a list of usernames: ["amit_01", "sneha123", "raj@kumar", "PRIYA"]. 
# Using a for loop and isalnum(), print each username 
# along with whether it is valid (only letters and numbers allowed).

usernames = ["amit_01", "sneha123", "raj@kumar", "PRIYA"]

for user in usernames:
    if user.isalnum():
        print(f"{user} -> Valid")
    else:
        print(f"{user} -> Invalid (only letters and number allowed)")