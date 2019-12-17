
#Matriz Beneficio Main
def matriz_beneficio(demanda, probabilidad, stock, venta, costo, venta_destemporada):
    matriz_principal = []
    matriz_valor_esperado = []
    matriz_beneficio = []
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
            cond_esp, esp, cond = calculo_beneficio(_demanda, _stock, costo, venta, probabilidad, index, venta_destemporada)

            #Matriz cond con Valor Esperado
            matriz_cond_esp.append(cond_esp)

            #Matriz Valor esperado
            matriz_esp.append(esp)

            #Matriz Cond (Beneficio)
            matriz_cond.append(cond)
        print('\n')
            
        matriz_total_valor_esperado.append(0)
        index += 1

        matriz_principal.append(matriz_cond_esp)
        matriz_beneficio.append(matriz_cond)
        matriz_valor_esperado.append(matriz_esp)
        
        # print(matriz_valor_esperado)
    print("===================================================================")
    mostrar_matriz_beneficio(matriz_beneficio)
    print("===================================================================")
    mostrar_matriz_valor_esperado(matriz_valor_esperado)
    print("===================================================================")
    suma_valor_esperado(matriz_valor_esperado, matriz_total_valor_esperado)
    print("===================================================================")


# Calcula el beneficio de la matriz
def calculo_beneficio(_demanda, _stock, costo, venta, probabilidad, index, venta_destemporada):
    cond = 0
    esp = probabilidad[index]
    cond_esp = []

    if _stock > _demanda:

        if venta_destemporada > 0:
            cond = ((_stock - (_stock - _demanda)) * (venta - costo)) + ( ((_stock - _demanda) * venta_destemporada) - ((_stock - _demanda) * costo)  )
            cond_str = ('((stock: %s - (stock: %s - demanda: %s)) * (venta: %s - costo: %s)) + ( ((stock: %s - demanda: %s) * venta_destemporada: %s) - ((stock: %s - demanda: %s) * costo: %s)  ) = %s' 
            % (_stock, _stock, _demanda, venta, costo, _stock, _demanda, venta_destemporada, _stock, _demanda, costo, cond))

        else:    
            cond = (venta * _demanda) - (costo * _stock)
            cond_str = 'Venta %s * Demanda %s - costo %s * Stock %s = %s' % (venta, _demanda, costo, _stock, cond)

        esp_str = 'Beneficio %s * Probabilidad %s'% (cond, esp)
        esp = cond * esp
        esp_str += ' = %s' % esp
        
    elif _stock <= _demanda:
        cond = (venta * _stock) - (costo * _stock)

        esp_str = 'Beneficio %s * Probabilidad %s'% (cond, esp)
        esp = cond * esp
        esp_str += ' = %s' % esp        
        cond_str = 'Venta %s * Stock %s - costo %s * Stock %s = %s' % (venta, _stock, costo, _stock, cond)
    
    print(cond_str)
    print(esp_str)
    cond_esp.append(cond)
    cond_esp.append(esp)
    return cond_esp, esp, cond



#Muestra matriz beneficio
def mostrar_matriz_beneficio(matriz_cond):
    print('\n\nMatriz Beneficio\n')
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


def calcula_valor_esperado(valor_esperado):
    ultimo_valor = 0
    stock = 0
    count_stock = 0
    for valor in valor_esperado:
        if valor >= ultimo_valor:
            ultimo_valor = valor
            stock = count_stock
        count_stock += 1
    print("\nEl Valor esperado es: %s y el stock es el %s \n" % (ultimo_valor, stock))


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
matriz_beneficio(demanda, probabilidad, stock, venta, costo, venta_destemporada)

# Para obtener el valor de la perfecta informacion se toma los valores 
# diagonales de la matriz beneficio, multiplicado por su probabilidad
# y restado con el valor esperado de la matriz beneficion, Todo eso debería ser igual al resultado
# esperado de la matriz de perdida
# ejemplo
# 3000(0,2)+4500(0,4)+5100(0,3)+5700(0,1)-4220 = 280