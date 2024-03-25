# Defining a definition to work with *args
def build_tuple(*args):
    return args


# Defining a tuple to work with
message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

# Defining another tuple to work with
number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)


# Looking into keyword arguments
# Defining a function to print something backwards
def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # Change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)      # Print the first word separately
    # print(end=end_character)  # Which means we don't need this line


# Different function to perform the operation
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


# Specifying the keyword arguments
with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

# Testing various outputs
print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
