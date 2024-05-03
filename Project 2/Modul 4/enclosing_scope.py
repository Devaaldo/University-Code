def outer(message):
    "ini adalah enclosing scope"
    def inner():
        "ini adalah local scope bagi inner function"
        print(message)
    
    inner()

outer("Test Message")