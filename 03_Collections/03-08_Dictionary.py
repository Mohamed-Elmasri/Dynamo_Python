# 1️⃣ Create a Dictionary

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

print(student)

# 2️⃣ Access a Value

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

print(student["name"])
print(student["grade"])

# 3️⃣ Modify a Value

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

student["grade"] = 95

print(student)

# 4️⃣ Add a New Key and Value

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

student["age"] = 20

print(student)

# 5️⃣ Delete a Key and Value

student = {
	"name"  : "Ali",
	"grade" : 90,
	"passed": True
}

del student["passed"]

print(student)
