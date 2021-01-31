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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

"""
要修改属性的值，最简单的方式是通过实例直接访问它。
"""
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


