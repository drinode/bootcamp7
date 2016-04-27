def data_type(x):
    '''
    Takes in an argument, x:
        -For an integer, return x ** 2
        -Fora float , return x / 2
        -For a string, returns "hello" + x
        -For a boolean, return "boolean"
        -For a long , return squareroot(x)
    '''
    if type(x) == int:
        return x ** 2
    elif type(x) == float:
        return x / 2
    elif type(x) == str:
        return "Hello {}".format(x)
    elif type(x) == bool:
        return "Boolean"
    elif type(x) == long:
        return "Long"
    else:
        return "That's not a  data type!"

print (data_type(17))
print (data_type(1.43))
print (data_type("Emmah"))
print (data_type(True))
print (data_type(False))


