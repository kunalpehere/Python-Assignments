# 4. Create a string path = "home/user/documents/notes.txt". 
# Using split(sep="/"), 
# print only the file name (the last part) using indexing.

path = "home/user/documents/notes.txt"

last_part = path.split(sep="/")

print("Last Part of Path:", last_part[3])