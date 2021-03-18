def make_pizza(*toppings):
    """
    形参名*toppings(糕点上的装饰材料)中的星号让Python创建一个名为toppings的空元组，
    并将收到的所有值都封装到这个元组中。
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

