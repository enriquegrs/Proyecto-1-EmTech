from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#Generamos una lista con los datos que necesitamos
procesaducto = [[prose[0], prose[3]] for prose in lifestore_products]
#print(f'\n{procesaducto}\n') # Obtenemos el ID de producto y categoria

cat = {}
for alp in procesaducto:
    bet = alp[0]
    gam = alp[1]
    if gam not in cat.keys():
        cat[gam] = []        
    cat[gam].append(bet)
#print(cat)

minventas = [[mini[0], mini[1]] for mini in lifestore_sales if mini[4]==0]
#print(minventas) #Obtenemos el ID de Venta y ID Pproducto

prot = {}
for n in minventas:
    id = n[0]
    cat = n[1]
    if cat not in prot.keys():
        prot[cat] = []        
    prot[cat].append(id)
#print(prot)

pcat = []

for c, z in prot.items():
    w = (len(z))
    prrlista = [c, w]
    pcat.append(prrlista)
    #if cosa != conteo:
        #print(cosa, len(conteo))

    #print(len(producto_ventas))
#print(f'{pcat}\n\n\n\n')
elementos_porcategoria = (len(pcat))
#print (elementos_porcategoria)

#Categorias (imprimimos las categorias con las mayores ventas)
process = pcat[0:8]  
t_video = pcat[8:17]  
t_madre = pcat[17:23]
driv_hd = pcat[23:31]
mem_ussb = pcat[31:32]
pantallas = pcat[32:35]
bocinas = pcat[35:36]
audifonos = pcat[36:40]


print(process)
# ############################################################################

process_ord = sorted(process, key= lambda x:x[1], reverse=True)
# t_video_ord = sorted(tarjetavideo, key=lambda a:a[1], reverse=True)
# t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=True)
# drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=True)
# mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
# pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=True)
# audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=True)
# #print(process_ord)

#print('PROCESADORES')
#print(f'\t{process}')
#print(f'\n5 Procesadores con mayores ventas: \n\n\t{process_ord[0:5]}\n')
# print('TARJETA DE VIDEO')
# print(f'\t{tarjetavideo}')
# print(f'\n5 Tarjetas de Video con mayores ventas son: \n\n\t{tarjetavideo_ord[0:5]}\n')
# print('TARJETA MADRE')
# print(f'\t{t_madre}')
# print(f'\n5 Tarjetas Madre con mayores ventas son: \n\n\t{t_madre_ord[0:5]}\n')
# print('DISCOS DUROS')
# print(f'\t{driv_hd}')
# print(f'\n5 Discos Duros con mayores ventas son: \n\n\t{drive_hd_ord[0:5]}\n')
# print('MEMORIAS USB')
# print(f'\t{mem_ussb}')
# print(f'\n5 Memorias USB con mayores ventas son: \n\n\t{mem_ussb_ord[0:5]}\n')
# print('PANTALLAS')
# print(f'\t{pantallas}')
# print(f'\n5 Pantallas con mayores ventas son: \n\n\t{pantallas_ord[0:5]}\n')
# print('AUDIFONOS')
# print(f'\t{audifonos}')
# print(f'\n5 Audifonos con mayores ventas son: \n\n\t{audifonos_ord[0:5]}\n')

# ###############################################################################################

# process_ord = sorted(process, key= lambda x:x[1], reverse=False)
# tarjetavideo_ord = sorted(tarjetavideo, key=lambda a:a[1], reverse=False)
# t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=False)
# drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=False)
# mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=False)
# pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=False)
# audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=False)
#print(process_ord)

# print('PROCESADORES')
# print(f'\t{process}')
# print(f'\n5 Procesadores con menores ventas son: \n\n\t{process_ord[0:5]}\n')
# print('TARJETA DE VIDEO')
# print(f'\t{tarjetavideo}')
# print(f'\n5 Tarjetas de Video con menores ventas son: \n\n\t{tarjetavideo_ord[0:5]}\n')
# print('TARJETA MADRE')
# print(f'\t{t_madre}')
# print(f'\n5 Tarjetas Madre con menores ventas son: \n\n\t{t_madre_ord[0:5]}\n')
# print('DISCOS DUROS')
# print(f'\t{driv_hd}')
# print(f'\n5 Discos Duros con menores ventas son: \n\n\t{drive_hd_ord[0:5]}\n')
# print('MEMORIAS USB')
# print(f'\t{mem_ussb}')
# print(f'\n5 Memorias USB con menores ventas son: \n\n\t{mem_ussb_ord[0:5]}\n')
# print('PANTALLAS')
# print(f'\t{pantallas}')
# print(f'\n5 Pantallas con menores ventas son: \n\n\t{pantallas_ord[0:5]}\n')
# print('AUDIFONOS')
# print(f'\t{audifonos}')
# print(f'\n5 Audifonos con menores ventas son: \n\n\t{audifonos_ord[0:5]}\n')