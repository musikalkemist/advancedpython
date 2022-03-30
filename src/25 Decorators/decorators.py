# Decorators wrap a function / class -> modify its behaviour

# Use cases:
#  - checking types
#  - timing
#  - wait
#  - check if user is logged in
#  - ...

def greetings(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Bye!")
    return wrapper


@greetings
def hello_valerio():
    print("Hello Valerio")


hello_valerio()






