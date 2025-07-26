materials = {"Concrete", "Steel", "Glass"}
print("Original:", materials)

materials.add("Wood")
print("After add:", materials)

materials.update(["Brick", "Marble"])
print("After update:", materials)

materials.remove("Brick")
print("After remove:", materials)

materials.discard("Plastic")
print("After discard:", materials)

materials.clear()
print("After clear:", materials)
