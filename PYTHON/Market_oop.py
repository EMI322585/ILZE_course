'''class Market:
    def __init__(self, name, time, pavilions):
        self.name = name
        self.time = time
        self.pavilion = [] #list of pavilions

    def add_pavilion(self, name):
        pavilion = {"name": name, "stores": {}}

ct = Market(name="Rīgas centrāltirgus", time="P-P:7:00-20:00", pavilions="Gaļa")
at = Market(name="Agenskalna tirgus", time="Slēgts", pavilions="Zivis",)
store =

print(Pavilion1.name)
print(Pavilion1.time)
print(Pavilion1.pavilions)
print()
print(Pavilion2.name)
print(Pavilion2.time)
print(Pavilion2.pavilions)
'''


class Market:
    def __init__(self, name, open_hours):
        self.name = name
        self.open_hours = open_hours
        self.pavilions = []  # list of pavilions

    def add_pavilion(self, name):
        pavilion = {'name': name, 'stores': []}
        self.pavilions.append(pavilion)

    def add_store(self, pavilion_name, store_name, store_description):
        ir_atrasts = False
        for pavilion in self.pavilions:
            if pavilion['name'] == pavilion_name:
                pavilion['stores'].append({'name': store_name, 'description': store_description})
                ir_atrasts = True
        if not ir_atrasts:
            raise ValueError('Paviljons nav reģistrēts: '.format(pavilion_name))

    def print(self):
        for pavilion in self.pavilions:
            print('\n') #tuksa rinda [ENTER]
            print('Paviljons: {}'.format(pavilion['name']))
            for veikals in pavilion['stores']:
                print('Veikals "{}": {}'.format(veikals['name'], veikals['description']))

ct = Market('Centraltirgus', '9.00 - 17.00')
ct.add_pavilion('Galas')
ct.add_store('Galas', 'Ribiņas', 'Garšīgas cūkas ribiņas')
ct.add_store('Galas', 'Jēri', 'Jēru gaļa')
ct.add_pavilion('Piena')
ct.add_store('Piena', 'Lauku sviests', 'Eko lauku sviests')
ct.add_store('Piena', 'SIA Biezpiens', 'Eko lauku biezpiens')

ct.print()
