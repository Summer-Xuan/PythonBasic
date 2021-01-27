"""
代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。这样的过程被称为重构。
重构让代码更清晰、更易于理解、更容易扩展。
"""
import json
filename = "demo/username.json"
def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            




def get_new_username():
    pass

def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
