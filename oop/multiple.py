class Car():
    total_car=0
    def __init__(self,model,brand):
        self.__model=model
        self.__brand=brand
        Car.total_car+=1

    def full_name(self):
        return f'{self.__brand} {self.__model}'
    
    def get_brand(self):
        return self.__brand

    def get_fuel_type(self):
        return 'pertrol or diseal'
    
    @staticmethod
    def generat_desc():
        return "Amazing"
    @property
    def model(self):
        return self.__model



class Engine:
    def engine_info(self):
        return 'this is engine'

class Battry:
    def battry_info(self):
        return 'this is battry'

class Electirc(Engine,Battry,Car):
    pass



E=Electirc('model s','tesla')
print(E.full_name())
print(E.battry_info())
print(E.engine_info())