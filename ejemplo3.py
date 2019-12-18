# -*- coding: utf-8 -*-

from inventario import *


# Costo de arranque O Costo fijo de orden DOLARES
K = 26
# Costo unitario de compra O Costo unitario de producción DOLARES
C = 6
# # Costo unitario ANUAL de Almacenamiento DOLARES
# H = 0.40
# Tasa de demanda anual ENTERO
lambda_ = 46000
# Dias en el Año ENTERO
dias_por_aaaa = 280
# #Dias de retraso ENTERO
# lead_time = 5
# #Inventario de seguridad en unidades ENTERO
# inventario_de_seguridad = 300
# # Costo unitario ANUAL de deuda DOLARES
P = 3.00
# Tasa de descuento ANUAL Porcetaje de descuento PORCIENTO
_i_ = 0.18
# #Tasa de relleno O unidades diarias de produccion ENTERO
# X = 480 


#DEMANDA DIARIA lambda
lamb_diario = demanda_diaria(lambda_, dias_por_aaaa)

#COSTO DE ALMACENAMIENTO
H_costo_almacenamiento_anual = costo_anual_tendencia_o_almacenamiento_h(C, _i_)

#COSTO DE ALMACENAMIENTO DIARIO
h_costo_almacenamiento_diario = costo_tendencia_diario_o_almacenamiento_h(H_costo_almacenamiento_anual, dias_por_aaaa)

# Politica optima de inventario
politica_optima_infinita = calcular_q(K, lambda_, P, H_costo_almacenamiento_anual)

#Inventario maximo
inv_maximo_infinita = calcular_y(K, lambda_, P, H_costo_almacenamiento_anual)

# Numero de ordenes anuales
orden(lambda_, politica_optima_infinita)

# Duracion de ciclo en dias T
T = duracion_lote(politica_optima_infinita, lamb_diario)

# # Duracion de ciclo en dias De relleno t
# _t_ = duracion_lote(politica_optima_infinita, inv_maximo_infinita)

#Ordenar z SI NO HAY DEMORA
ordenar_q_cuando_z(politica_optima_infinita, inv_maximo_infinita)

lead_time=3
# #Ordenar si hay demora en la entrega
# rop(lamb_diario, lead_time, politica_optima_infinita)

# # Inventario máximo DIARIO
# inv_maximo_infinita = inventario(H_costo_almacenamiento_anual, politica_optima_infinita, T)
# rop_entrega(T, 0.00386, lead_time, 0.017, lamb_diario, politica_optima_infinita)


#Si se demora 2 días en la entrega entonces el rop es
# lead_time = 1
# rop_entrega(T, _t_, lead_time, X, lamb_diario, politica_optima_infinita)

# #Costo Anual
# # costo_por_ciclo_infinito(K, C, politica_optima_infinita, H_costo_almacenamiento_anual, X, lamb_diario, T)
# costo_anual_infinito_diario(K, lambda_, lamb_diario, politica_optima_infinita, C, H_costo_almacenamiento_anual, X)

# # Si entran 55 unidades El tamaño optimo es
# # calcular_q_infinito(dias_por_aaaa*55, K, H_costo_almacenamiento_anual, X, lamb_diario)


# #Calcular nuevo lambda
# pol_opt = 800
# tasa_relleno = 500
# inv_max = 670
# dias_aaaa = 300
# calcular_lambda(pol_opt, inv_max, tasa_relleno, dias_aaaa)












# # • T = Duración de Ciclo
# # • t = Duración recepción
# # • Q = Tamaño de la orden
# # •  = Tasa de relleno

# # Demanda determinística y constante

# # print("\nDemanda determinística y constante")

# # politica_optima_de_inventario = politica_optima(K, lambda_, H_costo_almacenamiento_anual)

# # costo_anual(K, lambda_, politica_optima_de_inventario, C, H_costo_almacenamiento_anual)

# # duracion_en_dias = demanda_diaria(lambda_, dias_por_aaaa)

# # duracion_lote(politica_optima_de_inventario, duracion_en_dias) #o duracion del ciclo en dias

# # orden(lambda_, politica_optima_de_inventario) #Ordenes anuales

# # # ======================================

# # #No hay demora en la entrega
# # # print("\nNo hay demora en la entrega")

# # # _rop_ = rop(duracion_en_dias, lead_time, politica_optima_de_inventario)

# # # No hay inventario de seguridad
# # # print("\nNo hay inventario de segurida")

# # # inv_de_seguridad(politica_optima_de_inventario, _rop_, inventario_de_seguridad)

# # # # No hay descuentos por cantidad
# # # print("\nNo hay descuentos por cantidad")

# # # matriz_descuentos = [[[0, 499], 0.30], [[500, 999], 0.29], [[1000, 100000], 0.28]]
# # # recorrer_matriz_descuentos(matriz_descuentos, _i_, lambda_, K)


# # # print("\n• No se permiten atrasos")

# # # print("Q - Y aproximar al mayor")
# # # politica_opt_inventario = calcular_q(K, lambda_, P, H)
# # # calculo_de_y = calcular_y(K, lambda_, P, H)
# # # ordenar_q_cuando_z(politica_opt_inventario, calculo_de_y)


# # print("\n\n Tasa infinita de producción")
# # # costo_por_ciclo_infinito(K, c, q, h, x, lamb, t)
# # # costo_anual_infinito(k, lamb, q, c, h, x)

# # lamb_diario = demanda_diaria(lambda_, dias_por_aaaa)

# # politica_optima_infinita = calcular_q_infinito(lambda_, K, H, X, lamb_diario)
# # inventario_maximo(politica_optima_infinita, X, lamb_diario)

# # print("Diario")
# # calcular_t(politica_optima_infinita, lamb_diario)
# # print("Anual")
# # calcular_t(politica_optima_infinita, X)

