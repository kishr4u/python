from car import *

electric = ElectricCar("tesla","red",10,Electricity(5))
print(electric.name)
# no need to pass any argument. self taken on instance invocation
print(electric.get_name())

print(electric.battery_size)
print(electric.electricity.volt)