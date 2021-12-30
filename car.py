
#In python constructor is _init_ .. self is similar top java this.notice instance variables not declared
#notice self is passed to all method which is the instance. Overriding similar to java. also notice
#we dont specify type in return infact we dont specify type in args also as its dynamic type
class Car:
    def __init__(self,name, color):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name
    
    def print_car(self):
        print(f"car details are {self.name} , {self.color}")

class ElectricCar(Car):
    
    def __init__(self, name, color, size, electiricity):
        super().__init__(name, color)
        self.battery_size= size
        self.electricity = electiricity
        
    def print_car(self):
        print(f"car details are {self.name}, {self.color}, {self.battery_size} ")
    
    def set_battery_size(self, size):
        if(size < 10):
            print(" size less than 10 not allowed")
        else:
            self.battery_size = size
            
    #introduce a new variable
    def set_battery_color(self, color):
        self.battery_color=color
        
    
class Electricity:
     def __init__(self, volt):
        self.volt = volt
    
    