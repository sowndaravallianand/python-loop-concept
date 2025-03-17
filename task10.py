# Reverse a String Using a Loop

text = input("Enter a string: ")
reverse_text = ""
for char in text:
    reverse_text = char + reverse_text
print("Reversed string:", reverse_text)