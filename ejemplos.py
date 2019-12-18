# -*- coding: utf-8 -*-

from inventario import *

#Cantidad a ordenar
# # Tamaño de lote
# Q = 0 
# Costo de arranque 
# # Costo fijo de orden
# K = 5.50
# # Costo unitario de compra
# # Costo unitario de producción
# C = 2.00
# # Costo unitario ANUAL de Almacenamiento
# H = 0.40
# # Duracion de un lote
# T = 0
# # Tasa anual
# lambda_ = 10000
# # Dias en el Año
# dias_por_aaaa = 250
# #Dias de retraso
# lead_time = 5
# #Inventario de seguridad en unidades
# inventario_de_seguridad = 300



# # No hay descuentos por cantidad
# # print("\nNo hay descuentos por cantidad")
# #Ejemplo
# _K_ = 8
# _lambda_ = 600 #unidades anuales
# _i_ = 0.20

# print("\n• No se permiten atrasos")
#Ejemplo 2
# # Cantidad a ordenar
# Q1 = 0
# # Costo unitario anual de almacenamiento
# __lambda__ = 10000
# H1 = 0.40
# K1 = 5.5
# _dias_por_aaaa = 250
# # Costo unitario anual de deuda
# P = 2.00
# # Duración de un lote
# TDuracion = 0
# # Intervalo de disponibilidad
# TDisponibilidad = 0
# # Intervalo de escasez
# TEscacez = 0


# print("\n\n Tasa infinita de producción")





# Costo de arranque O Costo fijo de orden ENTERO
K = 5.50
# Costo unitario de compra O Costo unitario de producción DOLARES
C = 2.00
# Costo unitario ANUAL de Almacenamiento DOLARES
H = 0.40
# Tasa de demanda anual ENTERO
lambda_ = 10000
# Dias en el Año ENTERO
dias_por_aaaa = 250
#Dias de retraso ENTERO
lead_time = 5
#Inventario de seguridad en unidades ENTERO
inventario_de_seguridad = 300

# Tasa de demanda anual ENTERO
__lambda__ = 10000
# Costo unitario ANUAL de Almacenamiento DOLARES
H1 = 0.40
# Costo de arranque O Costo fijo de orden ENTERO
K1 = 5.5
# Dias en el Año ENTERO
_dias_por_aaaa = 250
# Costo unitario ANUAL de deuda DOLARES
P = 2.00

# Costo de arranque O Costo fijo de orden ENTERO
_K_ = 8
# Tasa de demanda anual ENTERO
_lambda_ = 600
# Porcetaje de descuento PORCIENTO
_i_ = 0.20
#Tasa de relleno O unidades diarias DEMANDA DIARIA ENTERO
X = 120 



# • T = Duración de Ciclo
# • t = Duración recepción
# • Q = Tamaño de la orden
# •  = Tasa de relleno

# Demanda determinística y constante

print("\nDemanda determinística y constante")

politica_optima_de_inventario = politica_optima(K, lambda_, H)

costo_anual(K, lambda_, politica_optima_de_inventario, C, H)

duracion_en_dias = demanda_diaria(lambda_, dias_por_aaaa)

duracion_lote(politica_optima_de_inventario, duracion_en_dias) #o duracion del ciclo en dias

orden(lambda_, politica_optima_de_inventario) #Ordenes anuales

# ======================================

#No hay demora en la entrega
print("\nNo hay demora en la entrega")

_rop_ = rop(duracion_en_dias, lead_time, politica_optima_de_inventario)

# No hay inventario de seguridad
print("\nNo hay inventario de segurida")

inv_de_seguridad(politica_optima_de_inventario, _rop_, inventario_de_seguridad)

# No hay descuentos por cantidad
print("\nNo hay descuentos por cantidad")

matriz_descuentos = [[[0, 499], 0.30], [[500, 999], 0.29], [[1000, 100000], 0.28]]

# descuento = 0.28
# calculo_h_con_descuento = h_con_descuento(_i_, descuento)
# resultado_eoq = eoq(_lambda_, _K_, calculo_h_con_descuento)

recorrer_matriz_descuentos(matriz_descuentos, _i_, _lambda_, _K_)


print("\n• No se permiten atrasos")

print("Q - Y aproximar al mayor")
politica_opt_inventario = calcular_q(K1, __lambda__, P, H1)
calculo_de_y = calcular_y(K1, __lambda__, P, H1)
ordenar_q_cuando_z(politica_opt_inventario, calculo_de_y)


print("\n\n Tasa infinita de producción")
# costo_por_ciclo_infinito(K1, c, q, h, x, lamb, t)
# costo_anual_infinito(k, lamb, q, c, h, x)

lamb_diario = demanda_diaria(lambda_, dias_por_aaaa)

politica_optima_infinita = calcular_q_infinito(__lambda__, K1, H1, X, lamb_diario)
inventario_maximo(politica_optima_infinita, X, lamb_diario)

print("Diario")
calcular_t(politica_optima_infinita, lamb_diario)
print("Anual")
calcular_t(politica_optima_infinita, X)