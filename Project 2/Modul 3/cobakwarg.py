def test_arguments(arg1, arg2, arg3):
    print("Argument 1 isinya adalah {}".format(arg1))
    print("Argument 2 isinya adalah {}".format(arg2))
    print("Argument 3 isinya adalah {}".format(arg3))

hello = {'arg1':"Cahyo",'arg2':"Coding",'arg3':"Cycling"}
test_arguments(**hello)