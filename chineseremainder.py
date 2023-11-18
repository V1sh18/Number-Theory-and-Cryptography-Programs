import numpy
def chinese_remainder(a, n):
    """
    Solves the Chinese Remainder Theorem.

    Args:
        a (list): A list of integers.
        n (list): A list of integers.

    Returns:
        int: The solution to the Chinese Remainder Theorem.
    """

    # Check if the input is valid.
    if len(a) != len(n):
        raise ValueError("The number of remainders must be the same as the number of moduli.")

    # Calculate the product of the moduli.
    M = int(numpy.prod(n))

    # Calculate the inverses of the moduli modulo the product of the moduli.
    M_inv = []
    for i in range(len(n)):
        M_inv.append(numpy.linalg.inv(n[i], M))

    # Calculate the solution.
    x = 0
    for i in range(len(n)):
        x += a[i] * M_inv[i] * M
    x %= M

    return x