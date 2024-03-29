import model
import text
import view
from copy import deepcopy

def find_contacts(message):
    search_word = view.input_data(message)
    result = model.phone_book.find_contact(search_word)
    view.show_contacts(result, text.find_contact_no_result(search_word))
    return True if result else False

def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                model.phone_book.open_phone_book()
                view.show_message(text.phone_book_opened_successful)

            case 2:
                model.phone_book.save_phone_book()
                view.show_message(text.phone_book_saved_successful)

            case 3:
                view.show_contacts(model.phone_book.phone_book, text.empty_phone_book_error)

            case 4:
                new_contact = view.input_data(text.input_new_contact)
                model.phone_book.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successful(new_contact[0]))

            case 5:
                find_contacts(text.input_search_word)

            case 6:
                if find_contacts(text.input_search_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = model.phone_book.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successful(name))

            case 7:
                if find_contacts(text.input_search_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = model.phone_book.delete_contact(u_id)
                    view.show_message(text.delete_contact_successful(name))

            case 8:
                if model.phone_book.first_phone_book != model.phone_book.phone_book:
                    user_choice = view.show_exit_menu()
                    if user_choice == 1:
                        model.phone_book.save_phone_book()
                        view.show_message(text.phone_book_saved_successful)
                break