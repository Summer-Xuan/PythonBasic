print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

"""
通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力.
依赖于try代码块成功执行的代码都放在else代码块中
"""
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except :  # ZeroDivisionError
        print("You can't divide by 0!")
    else:
        print(answer)



