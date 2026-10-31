string = "Дом, в котором мы живём, — это не просто дом. В доме живут люди, и люди эти делают дом домом. Без людей дом — просто стены, а стены без дома и без людей — уже не дом, а коробка."
for special_symbol in '!@#$%^&*()-_+=/-+/.,<>?";[]!№%:?`~—':
    string = string.replace(special_symbol, "")
filtred_string = string.lower()
words = filtred_string.split()
unusual_words = set(words)
print(f"Всего слов: {len(words)}, из них уникальных: {len(unusual_words)}")
dict_of_words = {}
for word in words:
    if word not in dict_of_words:
        dict_of_words[word] = 1
    else:
        dict_of_words[word] += 1
sort_of_dict = sorted(dict_of_words.items(), key=lambda item: (-item[1], item[0]))
top5words = []
count_of_5 = 0
for x, y in sort_of_dict:
    top5words.append([x, y])
    count_of_5 += 1
    if count_of_5 == 5: break
print(f"Топ-5 слов: {top5words[0][0]} ({top5words[0][1]}), {top5words[1][0]} ({top5words[1][1]}), {top5words[2][0]} ({top5words[2][1]}), {top5words[3][0]} ({top5words[3][1]}), {top5words[4][0]} ({top5words[4][1]})")
max_of_length = max(words, key = len)
all_max_words = ""
for word in words:
    if len(word) == max_of_length:
        all_max_words += word
        all_max_words += " "
print(f"Самое длинное слово/слова: {all_max_words}")
list_of_length = [len(word) for word in words]
dict_of_length = {}
for length in list_of_length:
    if length not in dict_of_length:
        dict_of_length[length] = 1
    else:
        dict_of_length[length] += 1
print("Слова по длинам: ", dict_of_length)