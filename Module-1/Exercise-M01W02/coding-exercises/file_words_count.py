def count_words(file_path: str) -> dict:
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result

if __name__ == "__main__":
    file_path = '/workspaces/AIO2024-MAIN/Module-1/Exercise-M01W02/P1_data.txt'
    print(count_words(file_path))