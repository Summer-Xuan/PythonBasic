"""
如果类自定义了__setattr__方法，当通过实例获取属性尝试赋值时，就会调用__setattr__。
常规的对实例属性赋值，被赋值的属性和值会存入实例属性字典__dict__中。
设置实例对象的一个新的属性时调用
"""
class ClassA(object):
    def __init__(self, classname):
        self.classname = classname


