def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(str_in)


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    return str_in[:1]


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    return str_in[-1]


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    return sub_str_in in str_in


# if str_in.find(sub_str_in) == -1:
#       return False
#   else:
#     return True


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    return str_in[start:stop]


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    a = ''
    for i in str_in:
        if i.isupper():
            a += i.lower()
        elif i.islower():
            a += i.upper()
    return a

# return str_in.swaps() # remove pass statement and implement me
# print(str_len('test'))
# print(input_has_substring("I am Beginner", "am"))
