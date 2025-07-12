# 1️⃣ insert() - Insert an item at a specific position
materials = ["Concrete", "Steel", "Glass"]
materials.insert(1, "Wood")  # Insert "Wood" at index 1
print("After insert:", materials)  # ['Concrete', 'Wood', 'Steel', 'Glass']

# 2️⃣ pop() - Remove item at a specific index
removed_item = materials.pop(2)  # Remove item at index 2
print("After pop:", materials)  # ['Concrete', 'Wood', 'Glass']
print("Removed item:", removed_item)  # Steel

# 3️⃣ sort() - Sort items alphabetically
materials.sort()
print("After sort:", materials)  # ['Concrete', 'Glass', 'Wood']

# 4️⃣ reverse() - Reverse the current order
materials.reverse()
print("After reverse:", materials)  # ['Wood', 'Glass', 'Concrete']

# 5️⃣ clear() - Remove all items from the list
materials.clear()
print("After clear:", materials)  # []

# 6️⃣ copy() - Create a copy of the list
original = ["Brick", "Sand", "Cement"]
copy_list = original.copy()
print("Original:", original)  # ['Brick', 'Sand', 'Cement']
print("Copy:", copy_list)  # ['Brick', 'Sand', 'Cement']
