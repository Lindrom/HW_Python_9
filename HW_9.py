import functools

contacts = {}

def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не найден"
        except ValueError:
            return "Неверный ввод. Пожалуйста, введите имя и телефон через пробел."
        except IndexError:
            return "Неверный ввод. Укажите имя."
    return wrapper

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Контакт успешно добавлен."

@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return "Контакт успешно обновлен."

@input_error
def get_phone(name):
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "Контакты не найдены."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def handle_command(command):
    if command.lower() == "hello":
        return "Могу я чем-нибудь помочь?"
    elif command.lower().startswith("add"):
        parts = command.split(" ", 2)
        if len(parts) < 3:
            raise ValueError
        name, phone = parts[1], parts[2]
        return add_contact(name, phone)
    elif command.lower().startswith("change"):
        parts = command.split(" ", 2)
        if len(parts) < 3:
            raise ValueError
        name, phone = parts[1], parts[2]
        return change_contact(name, phone)
    elif command.lower().startswith("phone"):
        parts = command.split(" ", 1)
        if len(parts) < 2:
            raise ValueError
        name = parts[1]
        return get_phone(name)
    elif command.lower() == "show all":
        return show_all_contacts()
    elif command.lower() in ["good bye", "close", "exit"]:
        return "До свидания!"
    else:
        return "Неверная команда. Пожалуйста, попробуйте еще ра."

def main():
    while True:
        command = input("Введите команду: ")
        response = handle_command(command)
        print(response)
        if response == "До свидания!":
            break

if __name__ == "__main__":
    main()