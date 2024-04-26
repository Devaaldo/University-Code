def outer(message):
    "ini adalah enclosing scope"
    def inner():
        "ini adalah local scope bagi inner function"
        print(message)
    return inner

outer_closure = outer("I'm a closure")
outer_closure()