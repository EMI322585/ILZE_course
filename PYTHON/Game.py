print('Sveiks/a! Šī ir "Slepenā skaitļa spēle"')
name = input("Lūdzu ievadi savu vārdu:")
print("Sveiks/a," + name)
from random import randint
number = randint(1,100)
print("Tagad mēģini uzminēt kādu skaitli no 1 līdz 100 esmu iedomājies un uzraksti to. Tev ir iespēja minēt 5 reizes. Lai veicas! ")

for x in range(5):
    guess = int(input("Ievadi skaitli:"))
    if guess == number:
        print("Apsveicu! Tu uzminēji! Skaitlis ir " + str(guess))
        break
    elif guess > number:
        print("Skaitlis ir mazāks.")
    elif guess < number:
        print("Skaitlis ir lielāks.")
else:
    print("Diemžēl Tu neuzminēji ar 5 minējumiem. Spēle beigusies!:(")