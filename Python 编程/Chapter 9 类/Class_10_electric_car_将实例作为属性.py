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


"""
使用代码模拟实物时，可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。
在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。可以将大型类拆分成多个协同工作的小类。
将小类实例用作大类的一个属性
"""
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)



class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        super()是一个特殊函数，帮助Python将父类和子类关联起来，
        下面一行代码让ElectricCar实例包含父类的所有属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """
        如果对电动汽车调用方法fill_gas_tank()，Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码
        假设Car类有一个名为fill_gas_tank()的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。电动汽车没有油箱
        """
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


