
def matriz_beneficio(demanda, stock, venta, compra):
    matriz_principal = []
    print('', stock)
    for _demanda in stock:
        matriz_1 = []
        matriz_respuesta = []
        for _stock in demanda:
            resultado = 0
            if _stock > _demanda:
                resultado = (venta * _demanda) - (compra * _stock)
                resultado_str = 'Venta %s * Demanda %s - Compra %s * Stock %s = %s' % (venta, _demanda, compra, _stock, resultado)
            elif _stock <= _demanda:
                resultado = (venta * _stock) - (compra * _stock)
                resultado_str = 'Venta %s * Stock %s - Compra %s * Stock %s = %s' % (venta, _stock, compra, _stock, resultado)
            
            print(resultado_str)
            matriz_1.append(resultado)
        # print(matriz_respuesta)
        print(_demanda, matriz_1)
        matriz_principal.append(matriz_1)


demanda = [0, 1, 2, 3, 4, 5]
stock = [0, 1, 2, 3, 4, 5]
venta = 30
compra = 20
matriz_beneficio(demanda, stock, venta, compra)