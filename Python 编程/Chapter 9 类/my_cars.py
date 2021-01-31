from car import Car, ElectricCar
import car
"""
需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法来访问类
"""

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
