"""
根据约定，在Python中，首字母大写的名称指的是类。
"""
class Dog():
    """一次模拟小狗的简单尝试"""
    """
    为何必须在方法定义中包含形参self呢？
    因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
    每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " roll over!")

# 1.创建多个实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)


# 1.访问属性
print("My dog's name is" + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age)+ 'years old.')

# 2.调用方法
my_dog.sit()
my_dog.roll_over()


# 1.访问属性
print("\nYour dog's name is" + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age)+ 'years old.')

# 2.调用方法
your_dog.sit()
your_dog.roll_over()
