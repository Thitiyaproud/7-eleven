
"""ooooooo"""

def print_7_eleven(number):
    if number % 77 == 0:
        return ("7-Eleven")
    elif number % 7 == 0:
        return ("Seven")
    elif number % 11 == 0:
        return ("Eleven")
    else:
        return (number)