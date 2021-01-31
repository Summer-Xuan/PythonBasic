class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """
        在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的；
        如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

"""
如果有更新属性的方法，将无需直接访问属性，
而可将值传递给一个方法，由它在内部进行更新。
"""
my_new_car.update_odometer(23)
my_new_car.read_odometer()


