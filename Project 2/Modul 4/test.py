# Variabel Global
x = "global"
def foo():
    print("x didalam adalah {}".format(x))
foo()
print("x diluar adalah {}" .format(x))


# Variabel Local
def foo():
    x = "local"
    print("x adalah variable {}".format(x))
foo()


# Non Local Variabel
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
outer()


