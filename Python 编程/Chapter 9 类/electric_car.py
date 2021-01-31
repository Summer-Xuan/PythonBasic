from car import Car
"""
在一个模块中导入另一个模块
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