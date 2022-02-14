from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import math


# Primero corresponde encontrar el promedio de precios
col_precio = []

for producto in lifestore_products:
    precio = producto[2]
    col_precio.append(precio)
## Imprimimos la columna a la cual hicimos referencia, aunque se encuentra en forma desordenada.
#print(col_precio)
# obtenemos el promedio
suma = sum(col_precio)
cuenta = len(col_precio)
promedio = suma/cuenta
# Imprimir promedio
#print(promedio)

# col_precios = [ producto[2] for producto in lifestore_products ]
# print(sum(col_precios) / len(col_precios))

# id_y_refund = [ [sale[0], sale[4]] for sale in lifestore_sales if sale[4] == 0]
#print(id_y_refund)

# for par in id_y_refund:
    #print(par)

# Dividir por meses las ventas
id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
# cateorizamos los datos
categorizacion_meses = {}

for par in id_fecha:
    # Obtenemos y el ID y la fecha correspondiente
    id = par[0]
    _, mes, _ = par[1].split('/')
    # Creamos el mes como una llave
    if mes not in categorizacion_meses.keys():
        categorizacion_meses[mes] = []
    categorizacion_meses[mes].append(id)



# for key in categorizacion_meses.keys():
    #print(key)
    #print(categorizacion_meses[key])


mes_info = {}

for mes, ids_venta in categorizacion_meses.items():
    lista_mes = ids_venta
    suma_venta = 0
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        info_prod = lifestore_products[id_product-1]
        precio = info_prod[2]
        suma_venta += precio
    #print(mes, suma_venta, f'ventas totales: {len(lista_mes)}')
    mes_info[mes] = [suma_venta, len(lista_mes)]



print('\nEl monto vendido por mes ordenado de mayor a menor es el siguiente:')
for id_product in mes_info.keys():
    lista_reviews = mes_info[id_product]
    promedio = sum(lista_reviews) / len(lista_reviews)
    # Ordenamos los numeros a cirfas con 2 decimales
    decimales = 2
    multiplicador = 10 ** decimales
    promedio = math.ceil(promedio * multiplicador) / multiplicador
    print(f' \n{id_product} ${promedio}')



mes_ganancia_ventas = []
for mes, datos in mes_info.items():
    ganancias, ventas = datos
    sub = [mes, ganancias, ventas]
    mes_ganancia_ventas.append(sub)

ord_mes = sorted(mes_ganancia_ventas)
ord_gancia = sorted(mes_ganancia_ventas, key=lambda x:x[1], reverse=True)
ord_ventas = sorted(mes_ganancia_ventas, key=lambda x:x[2], reverse=True)

# Ventas mensuales ordenadas de mayor a menor
print(f'\n A continuación se muestran los meses ordenados de mayor a menor con base en las unidades vendidas: \n{ord_ventas}\n ')

# Obtenemos el total de ventas en cantidad monetaria

alventas = [['04', 191066, 74], ['01', 117738, 52], ['03', 162931, 49], ['02', 107270, 40], ['05', 91936, 34], ['07', 26949, 11], ['06', 36949, 11], ['08', 3077, 3]]
total_ventas = [191066,117738,162931,107270,91936,26949,36949,3077]
print(f' Los ingresos totales corresponden a $ {(sum(total_ventas))}')

print(f' Obtenemos el total de unidades vendidas que corresponde en lo que va del año corresponde a 283 unidades.')

regr = [[reg[1], reg[4]] for reg in lifestore_sales if reg[4] == 1]
print(regr)

print('Las devoluciones suman 9 y corresponden al mismo numero de productos')
print(f'Por lo tanto la ventas totales netas son {283-9}')
