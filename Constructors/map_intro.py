# Define a variable to work with
text = "what have the romans ever done for us"


# Function to change the case of some input
def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


# Use the map() function go do the same
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


# Function to change the case of the words
def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


# Use the map() function to do the same
def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w


if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())
