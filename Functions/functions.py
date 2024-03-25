# Defining a function in Python using the def keyword
# Class and function definitions should be followed by two blank lines
def multiply():
    result = 10.5 * 4
    return result


# Using the function we defined
# To call a function, just use its name, with any arguments in parentheses
# Answer will be a float, since we multiply an int with a float
answer = multiply()
print(answer)


# Defining a new function, that takes in parameters
# Class and function definitions should also be preceded by two blank lines
def multiply_two(x, y):
    result = x * y
    return result


# Using the function we defined
answer_two = multiply_two(10, 4)
print(answer_two)

# Functions can be used anywhere the Python expects an expression
# As such, they can for example be used in a loop
for val in range(1, 5):
    two_times = multiply_two(2, val)
    print(two_times)


# Defining a function to check if a string is a palindrome
# A palindrome is a word that reads the same backwards as forwards
# The general syntax for slicing is start:end:step
# The colons represents the start and end indices of the slice
# Since no indices are provided, the slice includes the entire string
# The -1 specifies a negative step value, where the elements are iterated over in reverse order
# This function will return True or False, which will be the result the function returns
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# Using the new function we defined for words
word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))


# Defining a new function to check if an entire sentence is a palindrome
# The isalnum() method returns True if all characters are alphanumeric, allowing for both numbers and letters
# In this function, only alphanumeric characters are considered, by adding them to the string
# Here we have added function annotations for clarity and documentation
def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)

    return is_palindrome(string)


# Using the new function we defined for sentences
user_sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(user_sentence):
    print("{} is a palindrome".format(user_sentence))
else:
    print("{} is not a palindrome".format(user_sentence))
