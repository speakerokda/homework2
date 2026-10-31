def game_status(board):
    list_of_elements = []
    for line in board:
        for element in line:
            if element == ".":
                return "Игра продолжается"
            list_of_elements.append(element)
    if list_of_elements[0] == list_of_elements[4] == list_of_elements[8]:
        return f"{list_of_elements[0]} победил"
    elif list_of_elements[0] == list_of_elements[3] == list_of_elements[6]:
        return f"{list_of_elements[0]} победил"
    elif list_of_elements[0] == list_of_elements[1] == list_of_elements[2]:
        return f"{list_of_elements[0]} победил"
    elif list_of_elements[3] == list_of_elements[4] == list_of_elements[5]:
        return f"{list_of_elements[3]} победил"
    elif list_of_elements[6] == list_of_elements[7] == list_of_elements[8]:
        return f"{list_of_elements[6]} победил"
    elif list_of_elements[1] == list_of_elements[4] == list_of_elements[7]:
        return f"{list_of_elements[1]} победил"
    elif list_of_elements[2] == list_of_elements[5] == list_of_elements[8]:
        return f"{list_of_elements[2]} победил"
    elif list_of_elements[2] == list_of_elements[4] == list_of_elements[6]:
        return f"{list_of_elements[2]} победил"
    else:
        return "Ничья"
print(game_status([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]))