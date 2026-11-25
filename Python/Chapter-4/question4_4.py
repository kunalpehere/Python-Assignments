# 4. Create a string digits = "0123456789". Using slicing with a step value, print:
# a) all the even digits (02468)
# b) all the odd digits (13579)
# c) every third digit starting from 0 (0369)

digits = "0123456789"

print(digits[0:9+1:2])
print(digits[1:9+1:2])
print(digits[0:9+1:3])