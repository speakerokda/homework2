def pig_latin(string):
    words = [word for word in string.split()]
    words_new = []
    for word in words:
        if word[0] in "aeiou":
            word = word + "way"
            words_new.append(word)
        else:
            while word[0] not in "aeiou":
                word = word[1:] + word[0]
            words_new.append(word + "ay")
    new_string = ""
    for word in words_new:
        new_string = new_string + word + " "
    return new_string
print(pig_latin("hello world apple string"))