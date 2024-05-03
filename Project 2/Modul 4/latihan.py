def luas_segitiga(func) :
    def inner(a, t):
        if a <= 5 :
            a = 5
        if t <= 5 :
            t = 5
        return func(a, t)
    return inner

@luas_segitiga
def hasil(a, t):
    c = 1/2*a*t
    print(c)

hasil(4,2)