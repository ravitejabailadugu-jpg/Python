def outer():

    def inner():
        print("inner function")

    inner()
    inner()


outer()

inner() 