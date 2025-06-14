text = "  hello python  "

# len() → count all characters including spaces
print("Length:", len(text))

# strip() → remove spaces from start and end
print("Strip:", text.strip())

# upper() → convert all letters to uppercase
print("Upper:", text.upper())

# lower() → convert all letters to lowercase
print("Lower:", text.lower())

# capitalize() → only first letter uppercase
print("Capitalize:", text.capitalize())

# title() → first letter of each word uppercase
print("Title:", text.title())

# replace() → replace part of the string
print("Replace:", text.replace("python", "Dynamo"))

# in → check if a word exists inside the string
print("Is 'python' in text ?", "python" in text)

# not in → check if a word does NOT exist
print("Is 'Java' not in text ?", "Java" not in text)
