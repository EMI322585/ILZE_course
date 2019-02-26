from Storage_functions import *

file_name = 'lists.txt'

list = read_from_database(file_name)
print("Piezīmes:")
while True:
    print_introduction()
    choice = input('Jūsu izvēle: ... ')
    if choice.lower() not in ["r", "a", "d", "c", "x" ]:
        print('Jūst esat izdarījis kļūdainu izvēli!')
        continue  # veids kā izlaist visu tālāko cikla darbību un sākt vēlreiz no sākuma

    if choice.lower() == 'r':
        print('\n')  # tukša rindiņa uz ekrāna pārskatāmībai
        print('Jūsu saraksts!')
        print_list(list)

    if choice.lower() == 'a':
        print('Elementa pievienosana!')
        value = input('Lūdzu ievadiet kārtējo saraksta elementu: ... ')
        list.append(value)

    if choice.lower() == 'x':
        print('Paldies par darbu!')
        break

write_to_database(file_name, list)