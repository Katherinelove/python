import json
def get_new_username():
    username = input("what' your name?")
    filename = "username.json"
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
    return username

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except:
        return None
    else:
        return username
def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back!" + username)
    else:
        username=get_new_username()
        print("I will remeber you when you come back!")

greet_user()
