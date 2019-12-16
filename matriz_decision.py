
def matriz_beneficio(demanda, probabilidad, stock, venta, compra):
    matriz_principal = []
    
    print('', stock)
    index = 0
    for _demanda in stock:
        matriz_1 = []
        matriz_respuesta = []
        for _stock in demanda:
            cond = 0
            esp = probabilidad[index]
            cond_esp = []

            if _stock > _demanda:
                cond = (venta * _demanda) - (compra * _stock)
                esp = cond * esp
                
                cond_str = 'Venta %s * Demanda %s - Compra %s * Stock %s = %s' % (venta, _demanda, compra, _stock, cond)
            elif _stock <= _demanda:
                cond = (venta * _stock) - (compra * _stock)
                esp = cond * esp
                
                cond_str = 'Venta %s * Stock %s - Compra %s * Stock %s = %s' % (venta, _stock, compra, _stock, cond)
            
            print(cond_str)
            cond_esp.append(cond)
            cond_esp.append(esp)
            matriz_1.append(cond_esp)
            # matriz_1.append(cond)
            # matriz_1.append(esp)
        index += 1
        # print(matriz_respuesta)
        print(_demanda, matriz_1)
        matriz_principal.append(matriz_1)


demanda = [0, 1, 2, 3, 4, 5]
probabilidad = [0.1, 0.1, 0.2, 0.3, 0.2, 0.1]
stock = [0, 1, 2, 3, 4, 5]
venta = 30
compra = 20
matriz_beneficio(demanda, probabilidad, stock, venta, compra)