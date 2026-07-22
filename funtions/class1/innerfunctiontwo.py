def outer():
    print('outer fun started')


    def login():
        print('login sucess')
    def inner():
        print('inner fun')
    return inner


inner=outer()

print(inner)
print(type(inner))
inner()
inner()

        