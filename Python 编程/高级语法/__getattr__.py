"""
实例instance通过instance.name访问属性name，只有当属性name没有在实例的__dict__或它构造类的__dict__或基类的__dict__中没有找到，才会调用__getattr__。
当属性name可以通过正常机制追溯到时，__getattr__是不会被调用的。
"""

class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)


insA = ClassA('ClassA')
print(insA.__dict__) # 实例insA已经有classname属性了

print(insA.classname) # 不会调用__getattr__

print(insA.grade) # grade属性没有找到，调用__getattr__




