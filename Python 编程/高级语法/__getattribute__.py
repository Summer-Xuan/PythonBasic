"""
实例instance通过instance.name访问属性name，__getattribute__方法一直会被调用，无论属性name是否追溯到。
如果类还定义了__getattr__方法，除非通过__getattribute__显式的调用它，或者__getattribute__方法出现AttributeError错误，否则__getattr__方法不会被调用了。
如下所示，ClassA中定义了__getattribute__方法，实例insA获取属性时，都会调用__getattribute__返回结果，即使是访问__dict__属性
"""
class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

    def __getattribute__(self, attr):
        return('invoke __getattribute__', attr)

insA = ClassA('ClassA')
print(insA)