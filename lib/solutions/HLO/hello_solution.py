

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) is not str:
        raise ValueError("name should be of type str")
    return "Hello, {}!".format(friend_name)




