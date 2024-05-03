def outer(message):
    "ini adalah enclosing scope"
    def inner():
        "ini adalah local scope bagi inner function"
        message = "whoaaa…"
        print(message)

    inner()
    print(message)
outer("Test message")