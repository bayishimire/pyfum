# Prompt user to enter a string
user_input = input("Enter a string you want: ")

# Create translation table (mapping characters from one set to another)
translation_table = str.maketrans(
    "kajipotefuKAJIPOTEFU",
    "akijopetufAKIJOPETUF"
)

# Translate the input string using the translation table
translated_text = user_input.translate(translation_table)

# Print the translated result
print(translated_text)