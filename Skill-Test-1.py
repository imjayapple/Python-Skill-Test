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

#9. What is list comprehension, and provide an example of how to use it.

#10. Describe the difference between a shallow copy and a deep copy in Python.

#11. Explain the concept of "duck typing" in Python and provide an example.

#12. What are *args and **kwargs in Python, and how are they used in function arguments?

#13. What is the purpose of the enumerate function, and provide an example of how to use it.

#14. Describe the difference between a generator and a list in Python, and provide an example of using a generator.

#15. What is a context manager in Python, and how is it typically used? Provide an example using the with statement.