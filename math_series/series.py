def fibonacci(n):
    """
    Takes in one paramater (n) and returns the nth value in the fibonacci series
    """
    if n < 0:
        print("Sorry wrong input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Takes in one paramater() returns the nth value in the lucas numbers
    """
    if n < 0:
        print("Sorry wrong input")

    elif n == 0:
        return 2

    elif n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x, y):
    """
    Calling this function with no (optional) last two parameters will produce numbers from the fibonacci series, Calling it with the optional arguments of 2 and 1 will produce values from the lucas numbers.  Other values for the optional paramters will produce other series.
    """
    if n < 0:
        return "Sorry please enter valid input"
    if n == 1:
        return fibonacci(n)
    if y or x == 2:
        return lucas(n)
