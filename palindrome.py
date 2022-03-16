def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    temp_str = value.replace(" ", "").lower()
    if temp_str == temp_str[:: - 1]:
        return True
    else:
        return False


print(is_palindrome("Palindrome is hard to compile"))
