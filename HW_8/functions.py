import text
import os

phone_book = []
path = './directory.txt'

def console_output_data():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            res_line = line.replace('|', '  ')
            print(res_line.strip())
        file.close()
        os.system("pause")

def add_new_contact():
    global phone_book, path
    with open(path, 'r+', encoding='UTF-8') as file:
        file.write(input(text.AddNC_name) + '|')
        file.write(input(text.AddNC_adress) + '|')
        file.write(input(text.AddNC_phone) + '|' + '\n')
        file.close()

def find_contact():
    global phone_book, path
    with open(path, 'r+', encoding='UTF-8') as file:
        finding_contact = input(text.find_contact)

    for line in file:
        if finding_contact in line:
            print(line.replace('|', '  '))

    file.close()
    os.system("pause")

def edit_contact():
    global phone_book, path
    finding_contact = input(text.EditC_name)

    with open (path,'r+', encoding='UTF-8') as file:
        for line in file:
            if finding_contact in line:
                edit_contact_info = line.split('|')
                buff = line
                menu_input = input(text.EditC_to_edit)
                match menu_input:
                    case "1":
                        edit_contact_info[0] = input(text.EditC_name)
                    case "2":
                        edit_contact_info[1] = input(text.EditC_adress)
                    case "3":
                        edit_contact_info[2] = input(text.EditC_phone)
                        
        edited_conctact_info = "|".join(edit_contact_info)
        file.seek(0)  
        old_data = file.read()
        file.seek(0)  
        file.truncate()  
        new_data = old_data.replace(buff, edited_conctact_info)
        file.write(new_data)

def delete_contact():
    global phone_book, path
    finding_contact = input(text.DeleteC_surname)

    with open (path,'r+', encoding='UTF-8') as file:
        for line in file:
            if finding_contact in line:
                buff = line

        file.seek(0)  
        old_data = file.read()
        file.seek(0) 
        file.truncate()
        new_data = old_data.replace(buff, '')
        file.write(new_data)
