def check_value(func):
    def inner(a, b):
        if a == 0:
            print("nol dibagi berapapun akan nol")
        if b ==0:
            print("angka kedua adalah nol maka diganti satu")
            b = 1
        return func(a,b)
    return inner


@check_value
def div(a,b):
    c = a/b
    print(c)


#bagaimana apabila 4 dibagi 2
div(4,2)
#bagaimana apabila 0 dibagi 2
div(4,2)
#bagaimana apabila 2 dibagi 