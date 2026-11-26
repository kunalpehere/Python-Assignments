# 7. Create two variables product = "Headphones" and price = 1499. 
# Print the sentence "Headphones costs Rs. 1499" 
# by joining the values with +. 
# First try it without str() and 
# write a comment about the error, then fix it using str().

product = "Headphones"
price = 1499

sentence = product + " costs Rs. " + str(price)
print(sentence)

# Trried without str() raises: TypeError: can only concatenate str (not "int") to str
# print(product + " costs Rs. " + price)
