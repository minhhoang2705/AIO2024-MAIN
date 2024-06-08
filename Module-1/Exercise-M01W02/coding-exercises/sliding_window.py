def sliding_window(num_list: list[int], k: int) -> list[int]:
    result = []
    window = []
    length = len(num_list)
    # iterate through the num_list
    for i in range(length - k + 1):
        window = num_list[i:i+k]
        result.append(max(window))
    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(sliding_window(num_list, k))
