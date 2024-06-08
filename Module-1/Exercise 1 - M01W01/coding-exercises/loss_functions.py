import math
import random


def mean_squared_error(y_true, y_pred):
    return (y_true - y_pred) ** 2


def mean_absolute_error(y_true, y_pred):
    return abs(y_true - y_pred)


def root_mean_squared_error(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))


def main():
    num_samples = input("Input number of samples: ")
    # check if num_samples is an integer
    if not num_samples.isnumeric():
        print("Number of samples must be an integer")
        return

    loss_function = input("Input loss function: ")
    num_samples = int(num_samples)
    match loss_function:
        case "mse":
            for i in range(num_samples):
                target = random.uniform(0, 10)
                predict = random.uniform(0, 10)
                loss = mean_squared_error(target, predict)
                print(
                    f"Loss name: {loss_function}, sample: {i}, target: {target}, predict: {predict}, loss: {loss}"
                )
        case "mae":
            for i in range(num_samples):
                target = random.uniform(0, 10)
                predict = random.uniform(0, 10)
                loss = mean_absolute_error(target, predict)
                print(
                    f"Loss name: {loss_function}, sample: {i}, target: {target}, predict: {predict}, loss: {loss}"
                )
        case "rmse":
            for i in range(num_samples):
                target = random.uniform(0, 10)
                predict = random.uniform(0, 10)
                loss = root_mean_squared_error(target, predict)
                print(
                    f"Loss name: {loss_function}, sample: {i}, target: {target}, predict: {predict}, loss: {loss}"
                )


if __name__ == "__main__":
    main()
