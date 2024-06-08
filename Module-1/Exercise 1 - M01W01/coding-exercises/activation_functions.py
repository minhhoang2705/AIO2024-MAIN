import math


def is_number(x):
    # check if x is a number
    try:
        float(x)
    except ValueError:
        return False
    return True


def valid_function_name(func_name):
    # check if func_name is in ['sigmoid', 'relu', 'elu']
    if func_name in ["sigmoid", "relu", "elu"]:
        return True
    else:
        print(f"{func_name} is not supported")
        return False


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x: float) -> float:
    return max(x, 0)


def elu(x: float, alpha=1.0):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)


def main():
    """
    Takes user input for x and activation function and prints the result.
    """
    x = input("Input x: ")
    if is_number(x):
        activation_function = input("Input activation function: ")
        if not valid_function_name(activation_function):
            return
        else:
            match activation_function:
                case "sigmoid":
                    result = sigmoid(float(x))
                case "relu":
                    result = relu(float(x))
                case "elu":
                    result = elu(float(x))
                case _:
                    print(f"{activation_function} is not supported")
                    return
        print(f"{activation_function}: f({x}) = {result}")
    else:
        print(f"{x} is not a number")

if __name__ == "__main__":
    main()
