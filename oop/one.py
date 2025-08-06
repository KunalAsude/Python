class Car():
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def full_name(self):
        return f'{self.brand} {self.model}'


class Electric(Car):
    def __init__(self,model,brand,battry_size):
        super().__init__(model,brand)
        self.battry_size= battry_size



# my_car=Car('xc90','volvo')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


my_new_car = Electric('tesla','model s','85kwh')
print(my_new_car.battry_size)
print(my_new_car.full_name())