catalog1 = [
{"title": "Мастер и Маргарита", "author": "Булгаков",
"year": 1967, "genre": "роман", "on_loan": True},
{"title": "Евгений Онегин", "author": "Пушкин",
"year": 1833, "genre": "роман", "on_loan": False},
{"title": "Стихотворения", "author": "Есенин",
"year": 1926, "genre": "поэзия", "on_loan": False},
{"title": "Вишнёвый сад", "author": "Чехов",
"year": 1904, "genre": "пьеса", "on_loan": True},
{"title": "Руслан и Людмила", "author": "Пушкин",
"year": 1820, "genre": "поэма", "on_loan": False},
{"title": "Три сестры", "author": "Чехов",
"year": 1901, "genre": "пьеса", "on_loan": False},
]
def find_by_author(catalog, author):
    books = []
    for dic in catalog:
        if dic["author"] == author:
            books.append(dic["title"])
    return books
#print(find_by_author(catalog1, "Пушкин"))
def avaliable_titles(catalog):
    avaliable = []
    for book in catalog:
        if book["on_loan"] == False:
            avaliable.append(book["title"])
    return avaliable
#print(avaliable_titles(catalog1))
def books_grouped_by_genre(catalog):
    genres = {}
    for book in catalog:
        if book["on_loan"] == False:
            if book["genre"] not in genres:
                genres[book["genre"]] = [book["title"]]
            else:
                genres[book["genre"]].append(book["title"])
        else:
            continue
    return genres
#print(books_grouped_by_genre(catalog1))