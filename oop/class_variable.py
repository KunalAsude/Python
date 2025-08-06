class Car():
    total_car=0
    def __init__(self,model,brand):
        self.model=model
        self.__brand=brand
        Car.total_car+=1

    def full_name(self):
        return f'{self.__brand} {self.model}'
    
    def get_brand(self):
        return self.__brand

    def get_fuel_type(self):
        return 'pertrol or diseal'


class Electric(Car):
    def __init__(self,model,brand,battry_size):
        super().__init__(model,brand)
        self.battry_size= battry_size
    
    def get_fuel_type(self):
        return 'Electric Charge'





my_new_car = Electric('tesla','model s','85kwh')
Car('tata','safari')
print(Car.total_car)
