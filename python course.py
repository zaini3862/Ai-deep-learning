# Initialize an empty dictionary
user_dict = {}

# Prompt the user to enter five keys
for i in range(5):
    key = input(f"Enter key {i + 1}: ")
    # Prompt the user to enter the value for the current key
    value = input(f"Enter value for '{key}': ")
    # Add the key-value pair to the dictionary
    user_dict[key] = value

# Display the final dictionary
print("Final dictionary:", user_dict)
