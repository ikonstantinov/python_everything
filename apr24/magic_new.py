"""pattern Fabric"""


class Car:
    def run(self):
        print('Rrrrr')


class Truck:
    def run(self):
        print('Zhhhhh')


#фабричный класс, который порождает классы Car/Truck
class Vehicle:
    def __new__(cls, type_):
        if type_ == 'Car':
            return Car()
        elif type_ == 'Truck':
            return Truck()
        else:
            raise ValueError


vehicles = ['Car', 'Car', 'Truck', 'Car','Truck', 'Truck']
vehicles = [Vehicle(x) for x in vehicles]
#print(vehicles)
#print(type(vehicles))
for vehicle in vehicles:
    vehicle.run()