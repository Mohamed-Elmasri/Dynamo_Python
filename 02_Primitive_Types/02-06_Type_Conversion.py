# Implicit Conversion
a = 8
b = 2.5
c = a + b
print("Result:", c)  # Expected: 10.5

# Explicit Conversion - string to int
num_str = "15"
num_int = int(num_str)
print("After conversion:", num_int + 5)  # Expected: 20

# Explicit Conversion - float to int
pi = 3.99
rounded = int(pi)
print("Rounded down:", rounded)  # Expected: 3

# Explicit Conversion - int to string
score = 100
text = "Final Score: " + str(score)
print(text)  # Expected: Final Score: 100

# Explicit Conversion - string to float
rate_str = "1.5"
rate = float(rate_str)
print("Double:", rate * 2)  # Expected: 3.0

# Explicit Conversion - values to bool
print(bool(""))  # False
print(bool("Hi"))  # True
print(bool(0))  # False
print(bool(99))  # True
