class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
        
    def get_brand(self):
        return self.__brand + "!"
    
    def fullname(self):
        return f"{self.__brand} {self.__model}"
        
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are good"
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return "Electric charge"
        
# tesla=ElectricCar("tesla","S","6")
# print(tesla.fuel_type())

# print(isinstance(tesla,Car))
# print(isinstance(tesla,ElectricCar))


# mycar=Car("tata","Safari")
# mycar.model="nexon"
# print(mycar.model)

# print(mycar.general_description())
# print(Car.general_description())


class Battery:
    def battery_info(self):
        return "this battery" 

class Engine:
    def engine_info(self):
        return "this engine" 

class ElectricCarTwo(Battery, Engine, Car):
    pass

mynewcar=ElectricCarTwo("tesla","model s")

print(mynewcar.battery_info())
print(mynewcar.engine_info())