filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    """ 
    strip()去除字符串左右两侧的空字符串
    """
    pi_string += line.strip()

print(pi_string)
