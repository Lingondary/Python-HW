import functions
import view
import text

def start():
    while True:
        view.main_menu()
        user_input = input()
        if user_input == 0 and user_input > 6:
            return text.input_error
        match user_input:
            case "1":
                functions.console_output_data()
            case "2":
                functions.add_new_contact()
            case "3":
                functions.find_contact()
            case "4":
                functions.edit_contact()
            case "5":
                functions.delete_contact()
            case "6":
                break