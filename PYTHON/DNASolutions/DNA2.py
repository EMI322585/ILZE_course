people = {"eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

for person in people:
    suspect = True
    for prop in people[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect is True:
        print("{} is our perpetrator!".format(person.upper()))