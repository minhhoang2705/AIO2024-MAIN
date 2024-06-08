# write a function to calculate the precision, recall and f1 score
def calc_metrics(tp, fp, fn):
    # check each input is an integer
    if not isinstance(tp, int):
        raise TypeError("tp must be an integer")
    if not isinstance(fp, int):
        raise TypeError("fp must be an integer")
    if not isinstance(fn, int):
        raise TypeError("fn must be an integer")

    # check each input is non-negative
    if tp < 0 or fp < 0 or fn < 0:
        print("Inputs must be non-negative")
        return

    # check each input is non-zero
    if tp == 0 and fp == 0 and fn == 0:
        print("Inputs must be non-zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1: {f1}")


# Test the function
if __name__ == "__main__":
    calc_metrics(2, 3, 5)
    print(round(calc_metrics(2, 4, 5), 2))
