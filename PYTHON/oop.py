from datetime import datetime

class BasketballPlayer:
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(lebron)
'''class Human:
    def __init__(self,name,birth_year):
        self.full_name = name
        self.year_of_the_birth = birth_year
    def age(self, check_year=None):
        if not check_year:
            now = datetime.now()
            check_year = now.year
        return check_year - self.year_of_the_birth

janis = Human("Jānis", 1984)
anna = Human("Anna", 2000)

draugi = [janis, anna]

for draugs in draugi:
    print("{} age is {}".format(full_name, draugs.age()))
    print("{} age in 2035 will be {}".format(draugs.age(2035)))
'''