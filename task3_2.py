sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}
def revenue_of_day(day):
    if day not in sales.keys():
        return 'Неверный ввод или в этот день не работаем'
    else:
        revenue = 0
        best_position = ""
        count_of_position = 0
        for name, price, qty in sales[day]:
            revenue += price * qty
            if qty > count_of_position:
                count_of_position = qty
                best_position = name
        print(f"{day}: выручка {revenue}")
        if day != "Пятница" and day != "Среда":
            return f"Хит {day[:len(day) - 1]}а: {best_position}"
        else:
            return f"Хит {day[:len(day) - 1]}ы: {best_position}"
for day in sales.keys():
    print(revenue_of_day(day))