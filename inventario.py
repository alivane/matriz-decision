# -*- coding: utf-8 -*-
import math

# Demanda determinística y constante

def costo_por_ciclo(k, c, q, h, t):
    result = orden(k) + compra(c, q) + inventario(h, q, t)
    return result


def costo_anual(k, lamb, q, c, h):
    result = ( float(k*lamb)/ q ) + c * lamb + ( float(h * q) / 2)
    print("\n======================================")
    print("( (%s*%s)/ %s ) + %s * %s + ( (%s * %s) / 2) = %s" % (k, lamb, q, c, lamb, h, q, result))
    result = round(result)
    print("El costo anual de politica: %s " % result)
    print("======================================\n")
    return result


def orden(lamb, q):
    result = float(lamb / q)
    print("\n======================================")
    print("%s / %s = %s" % (q, lamb, result))
    print("El número de ordenes anuales es: %s " % result)
    print("======================================\n")
    return result


def compra(c, q):
    return float(c * q)


def inventario(h, q, t):
    result = float(h * q * t)/2
    return result

#Duracion del cliclo en días o duracion de lote
def duracion_lote(q, lamb):
    result = float(q / lamb)
    print("\n======================================")
    print("%s / %s = %s" % (q, lamb, result))
    print("La Duración del ciclo en días o la duración del lote es: %s dias " % result)
    print("======================================\n")
    return result


def demanda_diaria(lamb, dias):
    result = float(lamb / dias)
    print("\n======================================")
    print("%s / %s = %s" % (lamb, dias, result))
    print("La demanda diaria en días: %s " % result)
    print("======================================\n")
    return result


def politica_optima(k, lamb, h):
    result =  float(math.sqrt( float(2* k * lamb) / h))
    print("\n======================================")
    print("Raiz (2 * %s * %s ) / %s = %s" % (k, lamb, h, result))
    result = math.trunc(result)
    print("La politica óptima de inventario es: %s " % result)
    print("======================================\n")
    return result

#No hay demora en la entrega

def rop(lamb, lead_time, q):
    result = float(lamb * lead_time)
    print("\n======================================")
    print("%s * %s = %s" % (lamb, lead_time, result))
    print("Ordenar %s unidades cuando queden %s unidades en inventario "
         % (q, result))
    print("======================================\n")
    return result

def rop_entrega(t, t_menor, lead_time, x, lamb, q):
    if lead_time <= t_menor:
        result = float(t - lead_time) * float(x-lamb)
        print("\n======================================")
        print(" (%s - %s) * (%s-%s) = %s" % (t, lead_time, x, lamb, result))
        print("Ordenar %s Subiendo "
            % (result))
        print("======================================\n")
    else:
        print("Bajando")
        result = rop(lamb, lead_time, q)
    return result

def calcular_lambda(q, inv_max, x, d):
    result = float(x*d) - float(float(float(float(inv_max*x)/q))*d)
    print("\n======================================")
    print("(%s*%s) - ((%s/%s)*%s)*%s = %s" % (x, d, inv_max, q, x, d, result))
    print("El nuevo lambda es %s "% (result))
    print("======================================\n")
    return result

# No hay inventario de seguridad

def inv_de_seguridad(q, rop, seguridad):
    result = float(rop + seguridad)
    print("\n======================================")
    print("%s + %s = %s" % (rop, seguridad, result))
    print("Ordenar %s unidades cuando queden %s unidades en inventario "
         % (q, result))
    print("======================================\n")
    return result


# No hay descuentos por cantidad : Determinar el costo menor

def eoq(lamb, k, h):
    result = float(math.sqrt(float(2*lamb*k)/h))
    print("\n======================================")
    print("Raiz (2 * %s * %s) / %s = %s" % (lamb, k, h, result))
    result = math.trunc(result)
    print("El EOQ: %s " % result)
    print("======================================\n")
    return result

def costo_anual_tendencia_o_almacenamiento_h(c, i):
    result = float(c*i)
    print("\n======================================")
    print("%s* %s = %s" % (c, i, result))
    print("El Costo de Almacenamiento Anual H es: $%s " % result)
    print("======================================\n")
    return result

def costo_tendencia_diario_o_almacenamiento_h(h, dias_aaaa):
    result = float(h/dias_aaaa)
    print("\n======================================")
    print("%s/ %s = %s" % (h, dias_aaaa, result))
    print("El Costo de Almacenamiento Diario o Tendencia diaria Hd es: $%s " % result)
    print("======================================\n")
    return result

def h_con_descuento(h, descuento):
    result = float(h * descuento)
    print("\n======================================")
    print("%s * %s = %s" % (h, descuento, result))
    print("(%s) H es: %s " % (descuento, result))
    print("======================================")
    return result


def validar_factibilidad(matriz_descuentos, eoq, descuento, i, k, lamb):
    for row in matriz_descuentos:
        item = row[0]
        H = descuento * i
        
        if descuento == row[1]:
            if eoq >= item[0] and eoq <= item[1]:
                print("El EOQ %s Es factible" % eoq)
                print("Comparar costo anual de factible con los de puntos de quiebre,")
                costo_anual(k, lamb, eoq, descuento, H)
            else:
                print("El EOQ %s No es factible" % eoq)
                print("Comparar costo anual de factible con los de puntos de quiebre")
                quiebre = row[0][0]
                costo_anual(k, lamb, quiebre, descuento, H)
            print("Encontrar el mayor costo")


def recorrer_matriz_descuentos(matriz_descuentos, i, lamb, k):
    print("\n\n==================Validar Factibilidad====================\n\n")
    for row in matriz_descuentos:
        descuento = row[1]
        calculo_h_con_descuento = h_con_descuento(i, descuento)
        res_eoq = eoq(lamb, k, calculo_h_con_descuento)
        validar_factibilidad(matriz_descuentos, res_eoq, descuento, i, k, lamb)


def calcular_q(k, lamb, p, h):
    result = float(math.sqrt(float(2*k*lamb) / h)) * float(math.sqrt(float(p+h)/p))
    print("\n======================================")
    print("Raíz((2*%s*%s) / %s) * Raíz((%s+%s)/%s) = %s" % (k, lamb, h, p, h, p, result))
    print("(Q) El tamaño óptimo Con la deuda es: %s " % result)
    print("======================================\n")

    return result

#Inventario maximo
def calcular_y(k, lamb, p, h):
    result = float(math.sqrt(float(2*k*lamb) / h)) * float(math.sqrt(p/float(p+h)))
    print("\n======================================")
    print("Raíz((2*%s*%s) / %s) * Raíz(%s/(%s+%s)) = %s" % (k, lamb, h, p, p, h, result))
    print("(Y) El inventario maximo Con la deuda es: %s " % result)
    print("======================================\n")

    return result

def ordenar_q_cuando_z(q, y):
    result = float(q - y)
    print("\n======================================")
    print("%s - %s = %s" % (q, y, result))
    print("(Z) Si no hay demora demora en la entrega Ordenar %s cuando se deba %s " % (q, result))
    print("======================================\n")
    return result


#Taza infinita de producción

def inventario_maximo(q, x, lamb):
    result = float(q * float( float(x-lamb)/x ))
    print("\n======================================")
    print("%s * ( (%s-%s)/%s ) = %s" % (q, x, lamb, x, result))
    print("El inventario máximo con tasa de producción infinita es %s unidades" % result)
    print("======================================\n")
    return result


def costo_por_ciclo_infinito(k, c, q, h, x, lamb, t):
    result = float(k + c*q + h * float(q/2) * float( float(x-lamb)/x ) * t)
    print("\n======================================")
    print(" %s + %s*%s + %s * (%s/2) * ( (%s-%s)/%s ) * %s = %s" % (k, c, q, h, q, x, lamb, x, t, result))
    print("El costo por ciclo con tasa de producción infinita es %s " % result)
    print("======================================\n")
    return result


def costo_anual_infinito(k, lamb, q, c, h, x):
    result = float(float( float(k*lamb)/q ) + c*lamb + h * float(q/2) * float( float(x-lamb)/x ))
    print("\n======================================")
    print("( (%s*%s)/%s ) + %s*%s + %s * (%s/2) * ( (%s-%s)/%s ) = %s" % (k, lamb, q, c, lamb, h, q, x, lamb, x, result))
    print("El costo anual con tasa de producción infinita es %s " % result)
    print("======================================\n")
    return result

def costo_anual_infinito_diario(k, lamb, lamb_diario, q, c, h, x):
    result = float(float( float(k*lamb)/q ) + c*lamb + h * float(q/2) * float( float(x-lamb_diario)/x ))
    print("\n======================================")
    print("( (%s*%s)/%s ) + %s*%s + %s * (%s/2) * ( (%s-%s)/%s ) = %s" % (k, lamb, q, c, lamb, h, q, x, lamb_diario, x, result))
    print("El costo anual con tasa de producción infinita es %s " % result)
    print("======================================\n")
    return result

def calcular_q_infinito(lamb, k, h, x, lamb_diario):
    result = float(math.sqrt(float(2*lamb*k)/h)) * float(math.sqrt(x/float(x-lamb_diario)))
    print("\n======================================")
    print("Raíz ((2*%s*%s)/%s) * Raiz (%s/(%s-%s)) = %s" % (lamb, k, h, x, x, lamb_diario, result))
    print("Política óptima de inventario con tasa de producción infinita es %s " % result)
    print("======================================\n")
    return result

def calcular_t(q, lamb):
    result = float(q/lamb)
    print("\n======================================")
    print("%s/%s = %s" % (q, lamb, result))
    print("Política óptima de inventario con tasa de producción infinita es %s " % result)
    print("======================================\n")
    return result

