# 🔟 Predict the output of the following code and explain the difference between the values and their types.

a = 0b1010
b = 0o12
c = 0xA
print(a) # Output -> 10
print(b) # Output -> 10
print(c) # Output -> 10
print(type(a)) # Output -> <class 'int'> 
print(type(b)) # Output -> <class 'int'>
print(type(c)) # Output -> <class 'int'>

"""
Understand the Values
variable - a | type - Binary      | represented value - 0b1010 | Decimal Value - 10
variable - a | type - Octal       | represented value - 0o12 | Decimal Value - 10
variable - a | type - Hexadecimal | represented value - 0xA | Decimal Value - 10

Understanding the data types:- When Python reads these numbers, it automatically converts their representations into integer values.
Therefore:
type(a) returns int.
type(b) returns int.
type(c) returns int.
"""