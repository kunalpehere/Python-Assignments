# 9. Create a string message = "Meeting is on Monday at 10 AM". 
# Using replace(), change "Monday" to "Friday" and "10 AM" to "4 PM". 
# Print both the original and the new message, 
# and write a comment explaining why the original did not change.

message = "Meeting is on Monday at 10 AM"

new_message = message.replace("Monday", "Friday").replace("10 AM", "4 PM")

print("Original message:", message)
print("New message:", new_message)