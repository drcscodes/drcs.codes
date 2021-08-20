# '#' is the comment character in Python.
# Everything from # to end of line is ignored by Python interpreter

# Create a list by enclosing elements in []
boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
print("After boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']")
# Notice we have to convert the list to a string before concatenating
# with a string, otherwise we'd get a type error
print('boys == ' + str(boys))

# Can also create a list with list() constructor function
girls = list('Bebe', 'Wendy')
print("After girls = list('Bebe', 'Wendy')")
print("girls == " + str(girls))

# Access list elements by list position
print('boys[0] == ' + boys[0]) # prints Stan

# Notice that we have to put butters in a list.
# If we tried boys + 'Butters' we'd get a type error for trying to
# add a list to a string
boys + ['Butters']
print() # Blank like to make output more readable
print("After boys + ['Butters']")
print('boys == ' + str(boys))

# 'Butters' isn't in boys.  What happened?
# The + operator creates a new list, which we have to assign to a variable
more_boys = boys + ['Butters']
print()
print("After more_boys = boys + ['Butters']")
print('more_boys == ' + str(more_boys))

# If we want to add to the original list, we can assign to interpreter
boys = boys + ['Butters']
print()
print("After boys = boys + ['Butters']")
print('boys == ' + str(boys))


# Note that we can combine + and = with a shortcut assignment:
boys += ['Tweak']
print()
print("After boys += ['Tweak']")
print('boys == ' + str(boys))
