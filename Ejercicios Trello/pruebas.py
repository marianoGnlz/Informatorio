def confusa(x,y):
    x[0] = 1
    y[0] = y[0] + x[0]


lista = [4]
confusa(lista,lista)
print(lista)