print('Ingrese las ventas del primer día:', end=' ')
ventasDiaUno = int(input())
print('Ingrese las ventas del segundo día:', end=' ')
ventasDiaDos = int(input())

if (ventasDiaUno > ventasDiaDos):
    print('Hubo mas ventas en el primer día.')
elif (ventasDiaUno < ventasDiaDos):
    print('Hubo mas ventas en el segundo día.')
else:
    print('Hubo las misma cantidad de ventas en ambos dias.')