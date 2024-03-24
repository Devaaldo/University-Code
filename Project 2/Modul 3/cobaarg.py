def who_am_i(normal_parameter,*args):

    print("My name is {}".format(normal_parameter))
    for arg in args:
        print("My hobby is : {}".format(arg))

who_am_i("Cahyo","Coding","Cycling")