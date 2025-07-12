# 1️⃣ Create a List
materials = ["Concrete", "Steel", "Glass"]
print("Initial list:", materials)  # ['Concrete', 'Steel', 'Glass']

# 2️⃣ Access items by index
print("First item:", materials[0])  # Concrete
print("Second item:", materials[1])  # Steel
print("Last item:", materials[-1])  # Glass

# 3️⃣ Modify an item
materials[1] = "Wood"
print("After modification:", materials)  # ['Concrete', 'Wood', 'Glass']

# 4️⃣ Append an item to the end
materials.append("Brick")
print("After append:", materials)  # ['Concrete', 'Wood', 'Glass', 'Brick']

# 5️⃣ Remove an item by value
materials.remove("Glass")
print("After removal:", materials)  # ['Concrete', 'Wood', 'Brick']
