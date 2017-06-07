

def dec_func(orig_func):
    def wrapper():
        print("I'm a wrapper.")
        return orig_func()
    return wrapper

@dec_func
def display():
    print("Display func ran")

display()
