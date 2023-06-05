# Телефонный справочник, работает с форматом txt.
#
# 1. Открыть файл.V
# 2. Сохраняет файл. V
# 3. Показывает ТК. V
# 4. Добавить контакт.  V
# 5. Найти контакт. V   
# 6. Изменить контакт. V
# 7. Удалить контакт. V
# 8. Выход.

import os

def console_output_data():
    file = open('./directory.txt','r', encoding='UTF-8')
    while True:
        line = file.readline()
        if not line:
            break
        res_line = line.replace('|', '  ')
        print(res_line.strip())
    file.close()

def add_new_contact():
    file = open('./directory.txt','a', encoding='UTF-8')
    file.write(input("Введите фамилию и инициалы контакта: ") + '|')
    file.write(input("Введите адрес: ") + '|')
    file.write(input("Введите номер телефона: ") + '|' + '\n')
    file.close()

def find_contact():
    file = open('./directory.txt','r', encoding='UTF-8')
    finding_contact = input("Введите фамилию или телефон контакта: ")

    for line in file:
        if finding_contact in line:
            print(line.replace('|', '  '))

    file.close()

def edit_contact():

    finding_contact = input("Введите фамилию контакта: ")

    with open ('./directory.txt','r+', encoding='UTF-8') as file:
        for line in file:
            if finding_contact in line:
                edit_contact_info = line.split('|')
                buff = line
                menu_input = input("Что нужно изменить? \n 1. ФИО. \n 2. Адрес. \n 3. Телефон.\n")
                match menu_input:
                    case "1":
                        edit_contact_info[0] = input("Введите ФИО контакта: ")
                    case "2":
                        edit_contact_info[1] = input("Введите новый адрес контакта: ")
                    case "3":
                        edit_contact_info[2] = input("Введите новый телефон контакта: ")
                        
        edited_conctact_info = "|".join(edit_contact_info)
        file.seek(0)  
        old_data = file.read()
        file.seek(0)  
        file.truncate()  
        new_data = old_data.replace(buff, edited_conctact_info)
        file.write(new_data)

def delete_contact():

    finding_contact = input("Введите фамилию контакта: ")

    with open ('./directory.txt','r+', encoding='UTF-8') as file:
        for line in file:
            if finding_contact in line:
                buff = line

        file.seek(0)  
        old_data = file.read()
        file.seek(0) 
        file.truncate()
        new_data = old_data.replace(buff, '')
        file.write(new_data)

def main_menu():
    while True:
        print("У нас есть имитация справочника номеров в формате .txt, выберите действие:")
        print(" 1. Вывод справочника. \n 2. Добавить контакт. \n 3. Найти контакт. \n 4. Редактировать контакт. \n 5. Удалить контакт. \n 6. Выход.")
        user_input = input()
        match user_input:
            case "1":
                console_output_data()
            case "2":
                add_new_contact()
            case "3":
                find_contact()
            case "4":
                edit_contact()
            case "5":
                delete_contact()
            case "6":
                break
        os.system("pause")
main_menu()