def factorial(n):
    """
    n!
    """
    if n == 0:
        return 1
    else:
        result = n
        while n > 1:
            n -= 1
            result *= n
        return result


def approx_sin(x, n):
    """
    x: radian
    n: number of terms (n > 0)
    """
    result = 0
    for i in range(n):
        result += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
    return result

def approx_cos(x, n):
    """
    x: radian
    n: number of terms (n > 0)
    """
    result = 0
    for i in range(n):
        result += (-1) ** i * x ** (2 * i) / factorial(2 * i)
    return result

def approx_sinh(x, n):
    """
    x: radian
    n: number of terms (n > 0)
    """
    result = 0
    for i in range(n):
        result += x ** (2 * i + 1) / factorial(2 * i + 1)
    return result

def approx_cosh(x, n):
    """
    x: radian
    n: number of terms (n > 0)
    """
    result = 0
    for i in range(n):
        result += x ** (2 * i) / factorial(2 * i)
    return result

if __name__ == "__main__":
    print(approx_sin(3.14, 10))
    print(approx_cos(3.14, 10))
    print(approx_sinh(3.14, 10))
    print(approx_cosh(3.14, 10))