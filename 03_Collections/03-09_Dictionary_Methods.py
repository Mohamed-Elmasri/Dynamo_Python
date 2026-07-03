# 1️⃣ keys() - Return all keys

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

print(student.keys())

# Output:
# dict_keys(['name', 'grade', 'passed'])


# 2️⃣ values() - Return all values

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

print(student.values())

# Output:
# dict_values(['Ali', 90, True])


# 3️⃣ items() - Return all key-value pairs

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

print(student.items())

# Output:
# dict_items([('name', 'Ali'), ('grade', 90), ('passed', True)])


# 4️⃣ get() - Return the value of a key

student = {
	"name" : "Ali",
	"grade": 90
}

print(student.get("grade"))
print(student.get("age"))
print(student.get("age", "Key Not Found"))

# Output:
# 90
# None
# Key Not Found
