from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches



resultado = {}
for item in lifestore_sales:
    idproducto = str(item[1])
    if item[4] == 1:
        continue
    if idproducto in  resultado.keys():
        resultado[idproducto][0] = resultado[idproducto][0] + item[2]
        resultado[idproducto][1] = resultado[idproducto][1] + 1
    else:
        resultado[idproducto] = [item[2],1,0]

for key,value in resultado.items():
    resultado[key][2] = resultado[key][0]/resultado[key][1]

a = [{"nombre":"a","valor":3},{"nombre":"b","valor":5}]

listaResultado = list(resultado.items())

resutltado_ordenado = sorted(listaResultado,key= lambda x : x[1][2],reverse=True)

print("Los siguientes productos son aquellos que obtuvieron las mejores reseñas, con el formato (ID producto/ La suma de la calificación de reseñas/ La cantidad de reseñas/ El promedio de la reseñas)")
print(f'\n{resutltado_ordenado[0:5]}\n')


""" Realizamos la lista correspondiente a los productos con peores reseñas 
considerando los productos con devolucion.
"""

resultado = {}
for item in lifestore_sales:
    idproducto = str(item[1])
    # if item[4] == 0:
    #     continue
    if idproducto in  resultado.keys():
        resultado[idproducto][0] = resultado[idproducto][0] + item[2]
        resultado[idproducto][1] = resultado[idproducto][1] + 1
    else:
        resultado[idproducto] = [item[2],1,0]

for key,value in resultado.items():
    resultado[key][2] = resultado[key][0]/resultado[key][1]

a = [{"nombre":"a","valor":3},{"nombre":"b","valor":5}]

listaResultado = list(resultado.items())

resutltado_ordenado = sorted(listaResultado,key= lambda x : x[1][2],reverse=False)

print("Los siguientes productos son aquellos que obtuvieron las peores reseñas, con el formato (ID producto/ La suma de la calificación de reseñas/ La cantidad de reseñas/ El promedio de la reseñas)")
print(f'{resutltado_ordenado[0:5]}')



