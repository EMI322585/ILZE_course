import json

def print_introduction():
    print("Ja vēlies apskatīt sarakstu, nospied R (Read)")
    print("Ja vēlies papildināt sarakstu, nospied A (Add)")
    print("Ja vēlies iziet no saraksta, nospied X (Exit)")
    print("Ja vēlaties izdzēst kādu elementu, nospiediet D (Delete)")
    print("Ja vēlaties izdzēst visu sarakstu, nospiediet C (Clear)")

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
        print("{}.eleements ir {}".format(ix, item))
        ix += 1

def delete_from_list(list):
    delete = input("Lūdzu izvēlieties elementa kārtas nr, kuru vēlaties dzēst:")
    delete = int(delete)
    print("Jūs izvēlējāties elementu nr: " + str(delete))
    print("Vai tiešām vēlaties to dzēst? J/N")
    choice2 = input("Ievadiet J vai N:...")
    if choice2.lower() == "j":
        list.remove(str(delete))
        print("Elements ir izdzēsts.")
    if choice2.lower() == "n":
        print("Elements netika izdzēsts.")