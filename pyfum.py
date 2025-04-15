
# name = input("Enter your name: ")

# # Find the length of the name
# name_length = len(name)

# # Display the length of the name
# print(f"The length of your name is: {name_length}")
# Initialize an empty list to store the strings
strings = []

# Ask the user to enter five strings
for i in range(5):
    user_input = input(f"Enter string {i + 1}: ")
    strings.append(user_input)

# Find and display the length of each string
for i, string in enumerate(strings, 1):
    print(f"The length of string {i} ('{string}') is: {len(string)}")
