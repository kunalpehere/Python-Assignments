# 2. Create a string record = "Neha,22,Nagpur,BCA". 
# Using split(sep=","), separate the values and 
# print the name, age, city and course 
# on separate lines using indexing.

record = "Neha, 22, Nagpur, BCA"

separated_records = record.split(sep=",")

print("Name:",separated_records[0])
print("Age:",separated_records[1])
print("city:",separated_records[2])
print("course:",separated_records[3])