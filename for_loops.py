print("=== 1. ITERATING OVER A LIST ===")
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(f"I like {fruit}")

print("\n=== 2. ITERATING OVER A STRING ===")
word = "Python"
for letter in word:
    print(f"Letter: {letter}")

print("\n=== 3. USING RANGE() ===")
for i in range(10 + 1):
    print(f"Number: {i}")

print("\n=== 4. RANGE WITH START AND STOP ===")
for i in range(2, 8):
    print(f"Value: {i}")

print("\n=== 5. RANGE WITH STEP ===")
for i in range(0, 10, 2):
    print(f"Even: {i}") # even numbers 0 to 8

print("\n=== 6. ENUMERATE() - GET INDEX AND VALUE ===")
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Index: {index}: {color}")

print("\n=== 7. ITERATING OVER DICTIONARY ===")
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Just keys
for name in student_grades:
    print(f"Student: {name}")

print()
# Keys and values
for name, grade in student_grades.items():
    print(f"{name} scored {grade}")

print("\n=== 8. NESTED FOR LOOPS ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()  # new line after each row

print("\n=== 9. FOR LOOP WITH CONDITIONS ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

print("\n=== 10. BREAK AND CONTINUE ===")
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break     # stop at 7
    print(f"Processing: {i}")

print("\n=== 11. LIST COMPREHENSION (Alternative to for loop) ===")
# Traditional for loop
squares = []
for x in range(5):
    squares.append(x**2)
print(f"Squares (for loop): {squares}")

# List comprehension (more Pythonic)
squares_comp = [x**2 for x in range(5)]
print(f"Squares (comprehension): {squares_comp}")