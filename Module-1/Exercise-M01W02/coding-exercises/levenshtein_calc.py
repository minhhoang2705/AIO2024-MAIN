def levenshtein_distance(source, target):
    # đảm bảo rằng chuỗi source luôn dài hơn hoặc bằng chuỗi target để giảm thiểu việc sử dụng bộ nhớ
    if len(source) < len(target):
        source, target = target, source

    # Khởi tạo hàng trước (previous_row)
    previous_row = list(range(len(target) + 1))

    for i, s_char in enumerate(source, start=1):
        current_row = [i]
        for j, t_char in enumerate(target, start=1):
            insertions = previous_row[j] + 1
            deletions = current_row[j - 1] + 1
            substitutions = previous_row[j - 1] + (s_char != t_char)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


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
