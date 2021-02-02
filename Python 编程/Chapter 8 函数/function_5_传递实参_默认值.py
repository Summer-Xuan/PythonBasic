"""
编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用
指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略
相应的实参。
"""
"""
注意 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
这让Python依然能够正确地解读位置实参
"""
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print('\nI have a' + animal_type + '.')
    print('My' + animal_type + "'s name is" + pet_name.title() + '.')
describe_pet(pet_name='willie')