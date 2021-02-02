def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

"""调用返回值的函数时，需要提供一个变量，用于存储返回的值。"""
musician = get_formatted_name('jimi','hendrix')
print(musician)