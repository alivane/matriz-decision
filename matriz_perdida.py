
#Matriz Perdida Main
def matriz_perdida(demanda, probabilidad, stock, venta, costo, venta_destemporada):
    matriz_principal = []
    matriz_valor_esperado = []
    matriz_perdida = []
    matriz_total_valor_esperado = []

    print("===================================================================")
    print('Stock', stock)
    print('Demanda', demanda)
    print("===================================================================")
    print('Desarrollo')

    index = 0
    for _demanda in stock:
        matriz_cond_esp = []
        matriz_esp = []
        matriz_cond = []
        print('\n')
        for _stock in demanda:
            cond_esp, esp, cond = calculo_perdida(_demanda, _stock, costo, venta, probabilidad, index, venta_destemporada)

            #Matriz cond con Valor Esperado
            matriz_cond_esp.append(cond_esp)

            #Matriz Valor esperado
            matriz_esp.append(esp)

            #Matriz Cond (Perdida)
            matriz_cond.append(cond)
        print('\n')
            
        matriz_total_valor_esperado.append(0)
        index += 1

        matriz_principal.append(matriz_cond_esp)
        matriz_perdida.append(matriz_cond)
        matriz_valor_esperado.append(matriz_esp)
        
        # print(matriz_valor_esperado)
    print("===================================================================")
    mostrar_matriz_perdida(matriz_perdida)
    print("===================================================================")
    mostrar_matriz_valor_esperado(matriz_valor_esperado)
    print("===================================================================")
    suma_valor_esperado(matriz_valor_esperado, matriz_total_valor_esperado)
    print("===================================================================")


# Calcula el Perdida de la matriz
def calculo_perdida(_demanda, _stock, costo, venta, probabilidad, index, venta_destemporada):
    cond = 0
    esp = probabilidad[index]
    cond_esp = []

    if _stock == _demanda:
        cond = 0
        
        esp_str = 'Perdida %s * Probabilidad %s'% (cond, esp)
        esp = cond * esp
        esp_str += ' = %s' % esp
        cond_str = 'Stock es igual a la Demanda = 0'
    elif _stock <= _demanda:
        cond = (_demanda - _stock) * (venta - costo)

        esp_str = 'Perdida %s * Probabilidad %s'% (cond, esp)
        esp = cond * esp
        esp_str += ' = %s' % esp        
        cond_str = '(Demanda: %s - Stock: %s) * (Venta: %s - Costo: %s) = %s' % (_demanda, _stock, venta, costo, cond)
    else:
        if venta_destemporada > 0:
            cond = (_stock - _demanda)
            cond_str = '(Stock: %s - Demanda: %s) = %s' % (_stock, _demanda, cond)
        else:
            cond = (_stock - _demanda) * (costo)
            cond_str = '(Stock: %s - Demanda: %s) * Costo: %s = %s' % (_stock, _demanda, costo, cond)

        esp_str = 'Perdida %s * Probabilidad %s'% (cond, esp)
        esp = cond * esp
        esp_str += ' = %s' % esp        
    
    
    print(cond_str)
    print(esp_str)
    # cond_esp.append(cond)
    # cond_esp.append(esp)
    return cond_esp, esp, cond



#Muestra matriz Perdida
def mostrar_matriz_perdida(matriz_cond):
    print('\n\nMatriz Perdida\n')
    for row in matriz_cond:
        str_column = ''
        for column in row:
            if column < 0:
                str_column += ' %s   ' % column
            else:
                str_column += '  %s   ' % column
        print(str_column)


#Muestra matriz valor esperado
def mostrar_matriz_valor_esperado(matriz_esp):
    print('\n\nMatriz Valor Esperado\n')
    for row in matriz_esp:
        str_column = ''
        for column in row:
            if column < 0:
                str_column += ' %s   ' % column
            else:
                str_column += '  %s   ' % column
        print(str_column)


# Suma el valor esperado de toda la matriz
def suma_valor_esperado(valor_esperado, total_valor_esperado):
    for row in valor_esperado:
        count_index = 0
        for column in row:
            total_valor_esperado[count_index] += column
            count_index += 1
    print('\n\nTotal valor Esperado: ')
    print(total_valor_esperado)
    calcula_valor_esperado(total_valor_esperado)


#Calcula el valor esperado
def calcula_valor_esperado(valor_esperado):
    ultimo_valor = 1000000000000 #Valor de ejemplo
    stock = 0
    count_stock = 0
    for valor in valor_esperado:
        if valor <= ultimo_valor:
            ultimo_valor = valor
            stock = count_stock
        count_stock += 1
    print("\nEl Valor esperado es: %s y el stock es el %s \n" % (ultimo_valor, stock))


def perfecta_información():
    print("test")

# demanda = [0, 1, 2, 3, 4, 5]
# probabilidad = [0.1, 0.1, 0.2, 0.3, 0.2, 0.1]
# stock = [0, 1, 2, 3, 4, 5]
# venta = 30
# costo = 20
# venta_destemporada = 0

demanda = [1000, 1500, 1700, 1900]
probabilidad = [0.2, 0.4, 0.3, 0.1]
stock = [1000, 1500, 1700, 1900]
venta = 9
costo = 6
venta_destemporada = 5

matriz_perdida(demanda, probabilidad, stock, venta, costo, venta_destemporada)