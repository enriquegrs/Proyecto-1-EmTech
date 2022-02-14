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

#Traer searches 
meno_srch = [[srchs[0], srchs[1]] for srchs in lifestore_searches]
#print(meno_srch)

#Hacemos diccionario para clasificas las busquedas que  tiene cada producto
busq_x_prod = {}
for busq in meno_srch:
    id_srch = busq[0] 
    prod_srch = busq[1]
    if prod_srch not in busq_x_prod.keys():
        busq_x_prod[prod_srch] = []
    busq_x_prod[prod_srch].append(id_srch)
#print(busq_x_prod)

#Hacermos lista para conocer el numero de busquedasd por producto
lista_srchs = []

for k, v in busq_x_prod.items():
    ñ = (len(v))
    srchsilista = [k, ñ]
    lista_srchs.append(srchsilista)
    #if cosa != conteo:
        #print(cosa, len(conteo))

    #print(len(producto_ventas))
#print(f'{lista_srchs}\n\n\n\n')#Conocer el total numero de busquedas por ID PRODUCTO
elementos_porcategoria = (len(lista_srchs))
#print (elementos_porcategoria)

'''
LISTA DE CATEGORIAS
procesadores: [1, 2, 3, 4, 5, 6, 7, 8, 9]
tarjetas de video: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
tarjetas madre: [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
discos duros: [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
memorias usb: [60, 61]
pantallas: [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
bocinas: [74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
audifonos: [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
'''

#Categorias (imprimiendo las menores busquedas por cateogia)
srchs_process = lista_srchs[0:9]
srchs_t_video = lista_srchs[9:17]
srchs_t_madre = lista_srchs[17:23]
srchs_driv_hd = lista_srchs[23:31]
srchs_mem_ussb = lista_srchs[31:32]
srchs_pantallas = lista_srchs[32:35]
srchs_bocinas = lista_srchs[35:36]
srchs_audifonos = lista_srchs[36:40]
print(f'Las menores busquedas por categoria son la siguientes: {srchs_process} para cada Id de los procesadores.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_t_video} para cada Id de las tarjetas de video.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_t_madre} para cada Id de las tarjetas madre.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_driv_hd} para cada Id de los discos duros.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_mem_ussb} para cada Id de las memorias USB.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_pantallas} para cada Id de las pantallas.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_bocinas} para cada Id de las bocinas.\n')
print(f'Las menores busquedas por categoria son la siguientes: {srchs_audifonos} para cada Id de los audifonos.\n')

