import json

def print_introduction():
    print("Ja vēlaties apskatīt sarakstu, nospiediet R (Read)")
    print("Ja vēlaties pievienot piezīmi, nospiediet A (Add)")
    print("Ja vēlaties iziet no saraksta, nospiediet X (Exit)")
    print("Ja vēlaties izdzēst kādu piezīmi, nospiediet D (Delete)")
    print("Ja vēlaties izdzēst visu sarakstu, nospiediet C (Clear)")
    print("Ja vēlaties labot piezīmes saturu, nospiediet U (Update)")

def read_from_database(file_to_read):
    try:
        list = []
        with open(file_to_read, "r") as data_file:
            list = json.loads(data_file.read())
    except (ValueError, OSError):
        list = []
    return list

def write_to_database(file_to_write, data):
    with open(file_to_write, "w") as data_file:
        data_file.write(json.dumps(data))

def print_list(list):
    if len(list) == 0:
        print("Jūsu saraksts ir tukšs.")
        return None
    ix = 1
    for item in list:
        print("{}.piezīme ir {}".format(ix, item))
        ix += 1

def delete_from_list(list):
    delete = input("Lūdzu izvēlieties piezīmes kārtas nr, kuru vēlaties dzēst:")
    delete = int(delete)
    print("Jūs izvēlējāties piezīmi nr: " + str(delete))
    print("Vai tiešām vēlaties to dzēst? J/N")
    choice2 = input("Ievadiet J vai N:...")
    if choice2.lower() == "j":
        list.remove(str(delete))
        print("Piezīme ir izdzēsta.")
    if choice2.lower() == "n":
        print("Piezīme netika izdzēsta.")

def update_list(list):
    update = input("Lūdzu izvēlieties piezīmes nr, kuru vēlaties atzīmēt kā izdarītu")
    list.update(["Darīts"])
