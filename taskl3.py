def prefics(list):
    list_of_lengths = [len(word) for word in list]
    words = [word for word in list]
    min_len = min(list_of_lengths)
    answer = ""
    first_word = list[0]
    for length in range(min_len + 1):
        if all(word[:length] in first_word[:length] for word in words):
            answer = words[0][:length]
    return answer
print(prefics(["apple", "applj", "argon"]))