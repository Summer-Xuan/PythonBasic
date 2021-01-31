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

    def increment_odometer(self, mileage):
        "将里程表读数增加指定的量"
        if mileage >=0:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer!")



class ElectricCar(Car):
    """
    一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类
    电动汽车的独特之处

    """
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        super()是一个特殊函数，帮助Python将父类和子类关联起来，
        下面一行代码让ElectricCar实例包含父类的所有属性。
        """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


