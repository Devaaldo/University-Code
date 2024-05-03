def calon_decorator(func):
    def inner():
        print("Saya adalah calon dekorator")
        func()
    return inner


@calon_decorator
def fungsi():
    print("Saya adalah fungsi")

fungsi()
