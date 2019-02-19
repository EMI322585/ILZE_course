from list_functions import *

file_name = "list.txt"

list = read_from_database(file_name)

print("PIEZĪMES :)")
print()

while True:
    print_introduction()
    choice = input("Jūsu izvēle: ...")
    if choice.lower() not in ["r", "a", "x", "d", "c"]:
        print("Jūs esat izdarījis kļūdainu izvēli")
        continue #veids kā izlaist visu tālāko darbību un sākt ciklu no jauna

    if choice.lower() == "r":
        print("\n") # Tukša rindiņa uz ekrāna, pārskatāmībai
        print("Jūsu saraksts")
        print_list(list)

    if choice.lower() == "a":
        print("Elementa pievienošana")
        value = input("Lūdzu ievadiet kārtējo saraksta elementu:...")
        list.append(value)

    if choice.lower() == "d":
        print("Elementa dzēšana")
        delete_from_list(list)

    if choice.lower() == "c":
        print("Saraksta dzēšana")
        list.clear()

    if choice.lower() == "x":
        print("Paldies par darbu!")
        break

with open(file_name, "w") as data_file:
    data_file.write(json.dumps(list))


