def serie(limite):
    a = 0
    b = 1
    while a<limite:
        yield a
        a = b
        b = a+b
 
for numeros in serie(10):
        print (numeros)
    

