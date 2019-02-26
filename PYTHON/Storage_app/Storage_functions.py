import json  # JSON formāts, kas ļauj ērti pārvērst datus no LIST uz failā ierakstāmu STRING
             # JSON un LIST ir līdzīgi, bet ne vienādi!!!!


def print_introduction():

    print()
    print("Ja vēlaties apskatīt sarakstu, nospiediet R (Read)")
    print("Ja vēlaties papildināt sarakstu, nospiediet A (Add)")
    print("Ja vēlaties izdzēst kādu elementu no saraksta, nospiediet D (Delete)")
    print("Ja vēlaties izdzēst visu sarakstu, nospiediet C (Clear)")
    print("Ja vēlaties iziet no programmas, nospiediet X (Exit)")


def read_from_database(file_to_read):
    try:
        list = []
        with open(file_to_read, "r") as data_file:
            list = json.loads(data_file.read())
    except (ValueError, OSError):  # noķeram formāta vai faila neesamības kļūdu
        list = []  # Izveidojam tukšu sarakstu, ja nav izdevies ielasīt no faila
    return list


def write_to_database(file_to_write, data):
    with open(file_to_write, "w") as data_file:
        data_file.write(json.dumps(data))


def print_list(list):
    if len(list) == 0:
        print('Saraksts ir tukšs!')
        return None
    ix = 1
    for item in list:
        print('{}. elements ir: {}'.format(ix, item))
    ix += 1