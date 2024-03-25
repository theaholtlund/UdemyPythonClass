# Functions can also be defined with default arguments
# This modified banner function defines a screen width, along with a default argument
# We also add a docstring to document the function
# When annotating the parameters, we add spaces on each side of the equal sign
def modified_banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centered with ** on either side.

    :param text: The text to be formatted for the banner display.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** on either side).
    :raises: ValueError: if the provided string is too long ot fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


# Documentation, or docstrings, can also be accessed and printed
print(input.__doc__)
print("*" * 80)
print(modified_banner_text.__doc__)
print("*" * 80)
help(modified_banner_text)
print("*" * 80)

# Since default arguments are provided, there is no need to specify the screen width
# In this modified version, we also make it more intuitive what the code for the blank line does
# This was done by providing a default argument for the text value
modified_banner_text("*")
modified_banner_text("Always look on the bright side of life...")
modified_banner_text("If life seems jolly rotten,")
modified_banner_text("There's something you've forgotten!")
modified_banner_text("And that's to laugh and smile and dance and sing,")
modified_banner_text()
modified_banner_text("When you're feeling in the dumps,")
modified_banner_text("Don't be silly chumps,")
modified_banner_text("Just purse your lips and whistle - that's the thing!")
modified_banner_text("And... always look on the bright side of life...")
modified_banner_text("*")
