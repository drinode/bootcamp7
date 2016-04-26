def funky(a,b):
    if type(a) == str and type(b) == str:
        print (a + b)

    elif type(a) == int and type(b) == int:
        print (a + b)

    elif type(a) == float and type(b) == float:
        print (a + b)

    elif type(a) == list and type(b) == list:
        print (a + b) 

    else:
        print ("Ooops! Something went wrong")
funky("sage","python")
funky(1,2)
funky(1.2, 2.1)
funky([35,55,75,95],[25,50,35,60])
funky("sage", 8)
funky(4.5, 9)

a = {"model": "ferrari","color": "red"}
b = {"owner":"emma kimari", "year": 2015}
a.update(b)
print (a)