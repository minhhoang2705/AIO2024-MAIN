def count_letter_appearance(word: str) -> dict:
    result = {}
    for letter in word:
        if letter.isalpha():
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
    sorted_result = dict(sorted(result.items()))
    return sorted_result


if __name__ == "__main__":
    word = "Happiness"
    print(count_letter_appearance(word))
