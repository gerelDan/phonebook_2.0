import text

THEME = '='

def show_main_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.choice_main_menu_error)

def show_contacts(phone_book: dict[int, list[str]], error_message: str):
    if phone_book:
        max_len_name = 3 # Длина заголовка "Имя"
        max_len_phone = 7 # Длина заголовка "Телефон"
        max_len_comment = 11 # Длина заголовка "Комментарий"
        for value in phone_book.values():
            if len(value[0]) > max_len_name:
                max_len_name = len(value[0])
            if len(value[1]) > max_len_phone:
                max_len_phone = len(value[1])
            if len(value[2]) > max_len_comment:
                max_len_comment = len(value[2]) 
        len_theme = 11 + max_len_comment + max_len_phone + max_len_name
        print('\n' + THEME * len_theme)
        print(f'{"ID":>3}. {"Имя":<{max_len_name}} | {"Телефон":<{max_len_phone}} | {"Комментарий":<{max_len_comment}}')
        print(THEME * len_theme)
        for u_id, contact in phone_book.items():
            print(f'{u_id:>3}. {contact[0]:<{max_len_name}} | {contact[1]:<{max_len_phone}} | {contact[2]:<{max_len_comment}}')
        print(THEME * len_theme + '\n')
    else:
        show_message(error_message)

def show_message(message: str):
    print('\n' + THEME * len(message))
    print(message)

def input_data(message: str) -> list[str] | str:
    if isinstance(message, str):
        return input('\n' + message)
    return [input(mes) for mes in message]

def show_exit_menu():
    for i, item in enumerate(text.exit_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    
    while True:
        choice = input(text.choice_exit_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.exit_menu):
            return int(choice)
        print(text.choice_exit_menu_error)
