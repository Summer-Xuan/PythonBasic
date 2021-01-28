from name_function import get_formatted_name


"""编写一个使用这个函数的程序。程序names.py让用户输入名和姓，并显示整洁的全名"""
print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give me a first time")
    if first == 'q':
        break
    last = input("Please give me a last time")
    if last == 'q':
        break
    formatted_time = get_formatted_name(first, last)
    print("\tNeatly formatted name:" + formatted_time + '.')

