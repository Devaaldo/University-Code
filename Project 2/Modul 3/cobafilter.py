def multiply(x):
    numbers = list(range(5,21))
    return(numbers)

funcs = [multiply]
for i in range(1):
    value = list(map(lambda x:x(i),funcs))
    
    print(value)

def filternumb (num):
    
    if(num in angka):
        return True
    else:
        return False

angka = list(range(5,21))