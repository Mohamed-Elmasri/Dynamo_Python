# 1️⃣ len() - Get the number of items in the list
materials = ["Concrete", "Steel", "Glass", "Wood", "Brick"]
print("List Length:", len(materials))  # Output: 5

# 2️⃣ count() - Count how many times a value appears
colors = ["red", "blue", "green", "blue", "red", "red"]
print("How many 'red'?", colors.count("red"))  # Output: 3
print("How many 'blue'?", colors.count("blue"))  # Output: 2

# 3️⃣ extend() - Add multiple items at once
materials = ["Concrete", "Steel", "Glass"]
materials.extend(["Wood", "Brick"])
print("After extend:", materials)
# Output: ['Concrete', 'Steel', 'Glass', 'Wood', 'Brick']

# 4️⃣ Slicing - Get part of the list
print("materials[:3]  →", materials[:3])  # First 3 items
print("materials[1:]  →", materials[1:])  # From index 1 to end
print("materials[1:4] →", materials[1:4])  # From index 1 to 3
