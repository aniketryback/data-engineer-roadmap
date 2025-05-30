# Greatest Common Divisor (GCD) using Euclidean Algorithm

This Python function calculates the Greatest Common Divisor (GCD) of two non-negative integers using the efficient Euclidean Algorithm.

## Algorithm Explanation

The Euclidean Algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its remainder when divided by the smaller number. This process is repeated until one of the numbers becomes zero, at which point the other number is the GCD.

Mathematically, `GCD(a, b) = GCD(b, a % b)`.

## Python Implementation

```python
def GCD(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two non-negative integers
    using the Euclidean Algorithm.

    Args:
        a (int): The first non-negative integer.
        b (int): The second non-negative integer.

    Returns:
        int: The Greatest Common Divisor of a and b.
    """
    if b == 0:
        return a
    return GCD(b, a % b)
