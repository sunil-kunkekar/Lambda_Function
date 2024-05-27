# Lambda with a default argument value

power = lambda x, y=2: x ** y
print(power(3))   # Output: 9
# print(power(3, 3))  # Output: 27

#================================================================================================================
# List of dictionaries
students = [
    {'name': 'John', 'age': 25, 'grade': 'A'},
    {'name': 'Jane', 'age': 22, 'grade': 'B'},
    {'name': 'Dave', 'age': 20, 'grade': 'C'},
]
# Sort students by age
sorted_students = sorted(students, key=lambda student: student['age'])
sorted_students1 = sorted(students,key=lambda student:student['name'])
print(sorted_students1)  # Output: [{'name': 'Dave', 'age': 20,
print(sorted_students)
# Output: [{'name': 'Dave', 'age': 20, 'grade': 'C'}, {'name': 'Jane', 'age': 22, 'grade': 'B'}, {'name': 'John', 'age': 25, 'grade': 'A'}]





#==================================================================================================================================
# Use lambda functions to create a small calculator
calculator = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Error: Division by zero'
}
print(calculator['add'](10, 5))      # Output: 15
# print(calculator['divide'](10, 0))   # Output: Error: Division by zero

print(calculator['multiply'](2,25))


# add = lambda ad,bd : ad+bd 
# print(add(2,3))
#==============================================================================================
# Using a lambda function inside a list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x ** 2)(x) for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]


#=================================================================================
#Lambda Functions in Functional Programming
#Lambda functions are often used in functional programming alongside other functional programming constructs like map, filter, and reduce.
#map()
numbers = [1, 2, 3, 4]
double = list(map(lambda x: x * 2, numbers))
print(double)  # Output: [2, 4, 6, 8]


#===================================================

#filter()
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Output: [2, 4, 6]



#=================================================================
#reduce()
from functools import reduce
numbers = [1, 2, 3, 4]
sum     = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 10
