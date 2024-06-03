import math

# general formula of mean of nth root error
# md_nre = sum(math(sqrt(y_true, n) - math(sqrt(y_pred, n))) ** p) / num_samples


def md_nre_single_sample(y_true, y_pred, n, p):
    return (y_true ** (1 / n) - y_pred ** (1 / n)) ** p

if __name__ == "__main__":
    print(md_nre_single_sample(100, 99.5, 2, 1))