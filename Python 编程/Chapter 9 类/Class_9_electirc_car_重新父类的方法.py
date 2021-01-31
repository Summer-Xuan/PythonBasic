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
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        super()是一个特殊函数，帮助Python将父类和子类关联起来，
        下面一行代码让ElectricCar实例包含父类的所有属性。
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """
        如果对电动汽车调用方法fill_gas_tank()，Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码
        假设Car类有一个名为fill_gas_tank()的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。电动汽车没有油箱
        """
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


