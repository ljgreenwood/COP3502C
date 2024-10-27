def collatz_sequence(n):
    """
    If the number is even, the next number is n / 2.
    If the number is odd, the next number is 3 * n + 1.
    The sequence stops once it reaches 1.
    :param n:
    :return None - prints collatz sequence:
    """
    if n == 1:
        print(1)
        return
    if n % 2 == 0:
        print(round(n))
        collatz_sequence(n/2)
    else:
        print(round(n))
        collatz_sequence(3*n + 1)


def print_backwards(string, i=0):
    if len(string) == 1:
        return string  # base case
    else:
        if i == 0:
            print(string[-1] + print_backwards(string[:-1], i=i+1))
        else:
            return string[-1] + print_backwards(string[:-1], i=i+1)


def hammer_profit(cost, sale):
    """
    You will write a function that takes two arguments,
    the cost to produce a hammer, and the price that each hammer sold for.
    Your function should calculate the sum of the profits made on each hammer.
    """
    return sale[0] - cost + hammer_profit(cost, sale[1:]) if sale else 0


def format_names(names):
    if len(names) == 0:
        return names  # will pass out an empty list to be appended at the previous call
    current_name = names[0]
    if "," not in list(current_name):  # condition for reorganizing name
        exploded = current_name.split()
        current_name = exploded[1] + ", " + exploded[0]
    else:
        exploded = current_name.split(", ")
        current_name = exploded[0] + ", " + exploded[1]

    return [current_name] + format_names(names[1:])