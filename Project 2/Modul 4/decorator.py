def calon_decorator(func):
    def inner():
        print("Saya adalah calon dekorator")
        func()
    return inner

def fungsi():
    print("Saya adalah fungsi")

wrapped = calon_decorator(fungsi)
wrapped()