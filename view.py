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
        print('\n' + THEME * 71)
        for u_id, contact in phone_book.items():
            print(f'{u_id:>3}. {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}')
        print(THEME * 71 + '\n')
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
