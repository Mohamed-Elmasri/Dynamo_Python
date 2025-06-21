# Define variables
name = "Ali"
age = 25
salary = 10567.6596

# Old method using string concatenation
print("My name is " + name + " and I am " + str(age) + " years old")

# New method using formatted string
print(f"My name is {name} and I am {age} years old")

# Format salary with 2 decimal places
print(":.2f         =>", f"{salary:.2f}")  # Output: 10567.66

# Format salary with comma separator and 2 decimals
print(":,.2f        =>", f"{salary:,.2f}")  # Output: 10,567.66

# Round salary to nearest whole number
print(":.0f         =>", f"{salary:.0f}")  # Output: 10568
