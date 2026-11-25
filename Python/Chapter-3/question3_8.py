# 8. Create a string using triple quotes that contains 
# your name, your city and your favourite subject on three separate lines. 
# Print it. 
# Then write the same three lines using a single line string with 
# \ at the end of each line and print it. 
# Write a comment about the difference in the output.

# 1. Triple-quoted string (preserves actual newline characters)
info_multiline = """MySelf Kunal!
From Nashik
My favorite Subject is Object Oriented Programming"""

print(info_multiline)

print("-" * 40)

# 2. Single-line string using \ for line continuation in source code
info_singleline = "MySelf Kunal! \
From Nashik \
My favorite Subject is Object Oriented Programming"

print(info_singleline)

# Difference in output:
# Triple quotes (""" """) preserve line breaks, so the text prints across three separate lines.
# The backslash (\) only continues the code across lines in the editor without adding newline characters (\n), 
# so the output prints on a single continuous line.