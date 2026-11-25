# 10. A user enters their email with extra spaces: email = "    rahul.verma@gmail.com   ". 
# Print the email after using lstrip(), rstrip() and strip() separately, 
# and print len() each time to show how many characters were removed.

email = "    rahul.verma@gmail.com   "

original_len = len(email)
print(f"Original: '{email}' | Length: {original_len}")

left_stripped = email.lstrip()
print(
    f"After lstrip(): '{left_stripped}' | Length: {len(left_stripped)} "
    f"(Removed: {original_len - len(left_stripped)})"
)

right_stripped = email.rstrip()
print(
    f"After rstrip(): '{right_stripped}' | Length: {len(right_stripped)} "
    f"(Removed: {original_len - len(right_stripped)})"
)

both_stripped = email.strip()
print(
    f"After strip(): '{both_stripped}' | Length: {len(both_stripped)} "
    f"(Removed: {original_len - len(both_stripped)})"
)