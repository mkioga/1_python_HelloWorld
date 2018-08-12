# Python Strings and operators
print('Hello, World')
print(1+2)
print(7*3)
print()
print('The End')
print("Python's strings are easy to use")
print('We can even use "double quotes" in strings')
print("Hello" + "World")
# Now we will store the words in variables
greeting = "Hello"
name = "Bruce"
# Now we will print using the variables
print(greeting + name)
# Now we will add a space between greeting and name
print(greeting + ' ' + name)

# Now we will go to the next video
print()
print('Now we start video "Section 5, Lecture 21')
print ('Understanding more about python')
print()

# Using input function
greeting = "Hello"
name = input("Please Enter your name: ")
print (greeting + ' ' + name)
print()

# Using newline function to go to next line
splitstring = "This is the first line\nSecond line\nThird line"
print(splitstring)
print()

# Using tab function
tabbedstring = "Tab1\tTab2\tTab3\tTab4"
print(tabbedstring)
print()

# Using forward slash \ to print " and '
print('I want to use \"doublequote\" and \'singlequote\'')
print("I want to use \"doublequote\' and \'singlequote\'")
print()

# Using triple quotes """string""" to do split lines
anothersplitstring = """line one
line two
line three"""
print(anothersplitstring)
print()

# Using triple quotes to print ' and "
# Note that it has to start with triple quotes
# Make sure there are not 4 quotes in a row at the end, so use space
print(''' I want to use "doublequote" and 'singlequote' ''')
print(""" I want to use "doublequote" and 'singlequote' """)