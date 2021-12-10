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
    Calling this function with no (optional) last two parameters will produce numbers from the fibonacci series, Calling it with the optional arguments of 2 and 1 will produce values from the lucas numbers.  Other values for the optional paramters will produce other series.The required param wil determine which element in the series to print, and the second two optional params will have default values of 0 and 1 and determines the first two values for the series to be produced.  Calling with no optional params will return Fib because defaults are (0,1) calling it with (2,1) will produce the values from the Lucas function.
    """
    if n < 0:
        return "Sorry please enter valid input"
    if n == 1:
        return fibonacci(n)
    if y or x == 2:
        return lucas(n)
