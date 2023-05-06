#1. What is the difference between a list and a tuple in Python?
# • Lists are muttable in python, tuples are not.

#2. What is the purpose of the __init__ method in a Python class?
# • The purpose of the __init__ method is to initialize a new instance of a class when it is created.
# It allows you to set initial values for attributes, allocate resources, or perform any other setup
# tasks required for the object.

#3. How do you add an item to a set in Python?
# • Add items to a set by using the 'add()' method
# ex.
my_set = {1, 2, 3}
item_to_add = 4

my_set.add(item_to_add)
print(my_set)

#4. What is the output of the following code?
x = 10
def foo():
    x = 5
    print(x)

foo()
print(x)

# The code calls the function foo() which initializes the variable x with a value of 5 and prints said variable

#5. Write a simple function that takes a string as an input and returns the string reversed.
# Use the slice operator, 'start:end', the last index in the slice notation represents the step value, the interval
# between the elements that are included in the slice, default value of 1. By implementing '-1' it slices through every
# element in the sequence but in reverse order
def reverse_string(input_string):
    return input_string[::-1]

input_string = " dlrow olleh"
test_reverse_string = reverse_string(input_string)
print(test_reverse_string)
#6. What is a decorator in Python, and what is a common use case for them?
# Decorators are used to modify functions without changing its code
# ex. (below) timing_decorator takes a function "func" as input and returns a
# new function 'wrapper', which in this case adds a timing functionality
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def some_function():
    time.sleep(2)

some_function()

#7. Explain the difference between "pass", "continue", and "break" in Python.
# These terms are all a part of control flow statements.
# The "pass" statement is a no-operation (no-op) statement that does nothing when executed.
# The "continue" statement is used to skip the rest of the current iteration of the loop and proceed to the next iteration. 
# The "break" statement is used to exit the loop prematurely, i.e., to terminate the loop before it has completed all its iterations.

#8. How do you create a virtual environment in Python, and why would you use one?
# You create an isolated environment so that you can install packages and dependencies
# without interferring with the global python installation. Use the "venv" command.

#9. What is list comprehension, and provide an example of how to use it.
# List comprehensions are expressed as single line of code that allow users to generate a list
# ex. [expression for item in iterable if condition]
squares_of_evens = [x**2 for x in range(1, 11) if x % 2 == 0]

#10. Describe the difference between a shallow copy and a deep copy in Python.
# Shallow vs. Deep copies vary in the way they duplicate objects and their contents.
# Shallow: creates a new object, but does not create new instances of the objects within the original object.
# Deep: creates a new object and recursively creates new instances of the objects contained within the original object.

#11. Explain the concept of "duck typing" in Python and provide an example.
# It is a concept where the type or class of an object is less importantn than the methods & properties that it has.
# Emphasis on behaviour of the object rather than its inheritance.
# ex.
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
bird = Bird()

animal_speak(dog)  # Output: Woof!
animal_speak(cat)  # Output: Meow!
animal_speak(bird) # Output: Tweet!

#12. What are *args and **kwargs in Python, and how are they used in function arguments?
# They are a special syntax used in function arguments for passing a variable number of arguments to a function
# You can use *args & *kwargs to pass any number of positional or keyword arguments, respectively.
# *args
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3, 4)

# *kwargs
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example_function(a=1, b=2, c=3)

# *args & *kwargs
def example_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example_function(1, 2, 3, a=4, b=5, c=6)

#13. What is the purpose of the enumerate function, and provide an example of how to use it.

#14. Describe the difference between a generator and a list in Python, and provide an example of using a generator.

#15. What is a context manager in Python, and how is it typically used? Provide an example using the with statement.