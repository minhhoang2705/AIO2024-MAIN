def levenshtein_distance(source, target):
    # Bước 1: Xây dựng ma trận lưu trữ
    rows = len(source) + 1
    cols = len(target) + 1
    D = [[0 for _ in range(cols)] for _ in range(rows)]

    # Bước 2: Hoàn thiện hàng và cột đầu tiên
    for i in range(1, rows):
        D[i][0] = i
    for j in range(1, cols):
        D[0][j] = j

    # Bước 3: Tính toán các giá trị với các ô còn lại trong ma trận
    for i in range(1, rows):
        for j in range(1, cols):
            del_cost = D[i-1][j] + 1
            ins_cost = D[i][j-1] + 1
            sub_cost = D[i-1][j-1] + (0 if source[i-1] == target[j-1] else 1)
            D[i][j] = min(del_cost, ins_cost, sub_cost)

    # Bước 4: Trả về giá trị tại ô cuối cùng của ma trận
    return D[rows-1][cols-1]


if __name__ == "__main__":
    source = "kitten"
    target = "sitting"
    print(levenshtein_distance(source, target))  # Output: 3

    source = "yu"
    target = "you"
    print(levenshtein_distance(source, target))  # Output: 1

    source = "flaw"
    target = "lawn"
    print(levenshtein_distance(source, target))  # Output: 2
