phone_book = {}
path = 'phonebook.txt'
SEPARATOR = ';'

def open_phone_book():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)

def save_phone_book():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def _next_uid():
    global phone_book
    return max(phone_book) + 1 if phone_book else 1

def add_new_contact(new_contact: list[str]):
    global phone_book
    phone_book[_next_uid] = new_contact

def find_contact(search_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if search_word.lower() in ' '.join(contact).lower():
            result[u_id] = contact
    return result

def edit_contact(u_id: int, edited_contact: list[str]) -> str:
    '''
    Функция изменит контакт в телефонной книге
    '''
    global phone_book
    current_contact = phone_book[u_id]
    for i in range(len(current_contact)):
        current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
    phone_book[u_id] = current_contact
    return current_contact[0]

def delete_contact(u_id: int) -> str:
    global phone_book
    return phone_book.pop(u_id)[0]

