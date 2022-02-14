from lifestore_file import *
import math


def login():
    """
    Login:

    usuario:
        enriquegarcia
    contraseña:
        elrobotbueno123

    """



    Accessocorrecto = False
    intentos = 0


    #Bienvenida

    mensaje_bienvenida = 'Bienvenido al Sistema! \n Ingresa tus credenciales'
    print(mensaje_bienvenida)

    #Recibo los intentos realizados

    while not Accessocorrecto:
        # Ingresa tu usuario y contraseña
        usuario = input('Usuario: ')
        contrasena = input('Contraseña: ')
        intentos += 1
    # Validadción de los datos de inicio de sesión
        if usuario == 'enriquegarcia' and contrasena == 'elrobotbueno123':
            intentos -=1
            Accessocorrecto = True
            print('Hola!, bienvenido.')
    # En caso de que los datos sean incorrectos será denegado el acceso
        else:
            if usuario == 'enriquegarcia':
                print('El usuario o contraseña son incorrectos.')
                print('Te restan', 3 - intentos, 'intentos.')
            else:
                print('El usuario y contraseña son incorrectos.')
                print('Te restan', 3 - intentos, 'intentos.')
    # Unicamente se tiene 3 intentos para poder ingresar
        if intentos == 3:
            print('Intentalo más tarde.')
            exit()

def ejercicio1():
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
    #elementos_porcategoria = (len(pcat))
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


    #print(process)
    # ############################################################################

    process_ord = sorted(process, key= lambda x:x[1], reverse=True)
    t_video_ord = sorted(t_video, key=lambda a:a[1], reverse=True)
    t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=True)
    drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=True)
    mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=True)
    pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=True)
    bocinas_ord = sorted(bocinas, key=lambda g:g[1], reverse=True)
    audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=True)
    #print(process_ord)

    print('PROCESADORES')
    #print(f'\t{process}')
    print(f'\n5 Procesadores con mayores ventas: \n\n\t{process_ord[0:5]}\n')
    print('TARJETA DE VIDEO')
    # print(f'\t{tarjetavideo}')
    print(f'\n5 Tarjetas de Video con mayores ventas son: \n\n\t{t_video_ord[0:5]}\n')
    print('TARJETA MADRE')
    # print(f'\t{t_madre}')
    print(f'\n5 Tarjetas Madre con mayores ventas son: \n\n\t{t_madre_ord[0:5]}\n')
    print('DISCOS DUROS')
    # print(f'\t{driv_hd}')
    print(f'\n5 Discos Duros con mayores ventas son: \n\n\t{drive_hd_ord[0:5]}\n')
    print('MEMORIAS USB')
    # print(f'\t{mem_ussb}')
    print(f'\n5 Memorias USB con mayores ventas son: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    # print(f'\t{pantallas}')
    print(f'\n5 Pantallas con mayores ventas son: \n\n\t{pantallas_ord[0:5]}\n')
    print('BOCINAS')
    print(f'\n5 Bocinas con mayores ventas son: \n\n\t{bocinas_ord[0:5]}\n')
    print('AUDIFONOS')
    #print(f'\t{audifonos}')
    print(f'\n5 Audifonos con mayores ventas son: \n\n\t{audifonos_ord[0:5]}\n')

    # Ademas los 5 producto mas vendidos son 
    masvent=[[54,50],[3,42],[5,20],[42,18],[57,15]]
    print(f' Los 5 productos mas vendidos son los siguientes(ID, N. de Ventas):\n{masvent}\n')

    # ###############################################################################################

    process_ord = sorted(process, key= lambda x:x[1], reverse=False)
    tarjetavideo_ord = sorted(t_video, key=lambda a:a[1], reverse=False)
    t_madre_ord = sorted(t_madre, key=lambda b:b[1], reverse=False)
    drive_hd_ord = sorted(driv_hd, key=lambda c:c[1], reverse=False)
    mem_ussb_ord = sorted(mem_ussb, key=lambda d:d[1], reverse=False)
    pantallas_ord = sorted(pantallas, key=lambda e:e[1], reverse=False)
    audifonos_ord = sorted(audifonos, key=lambda f:f[1], reverse=False)
    #print(process_ord)

    print('PROCESADORES')
    # print(f'\t{process}')
    print(f'\n5 Procesadores con menores ventas son: \n\n\t{process_ord[0:5]}\n')
    print('TARJETA DE VIDEO')
    # print(f'\t{tarjetavideo}')
    print(f'\n5 Tarjetas de Video con menores ventas son: \n\n\t{tarjetavideo_ord[0:5]}\n')
    print('TARJETA MADRE')
    # print(f'\t{t_madre}')
    print(f'\n5 Tarjetas Madre con menores ventas son: \n\n\t{t_madre_ord[0:5]}\n')
    print('DISCOS DUROS')
    # print(f'\t{driv_hd}')
    print(f'\n5 Discos Duros con menores ventas son: \n\n\t{drive_hd_ord[0:5]}\n')
    print('MEMORIAS USB')
    # print(f'\t{mem_ussb}')
    print(f'\n5 Memorias USB con menores ventas son: \n\n\t{mem_ussb_ord[0:5]}\n')
    print('PANTALLAS')
    # print(f'\t{pantallas}')
    print(f'\n5 Pantallas con menores ventas son: \n\n\t{pantallas_ord[0:5]}\n')
    print('AUDIFONOS')
    # print(f'\t{audifonos}')
    print(f'\n5 Audifonos con menores ventas son: \n\n\t{audifonos_ord[0:5]}\n')

    # Ademas los 5 producto menos vendidos son 
    menosvent=[[66,1],[67,1],[84,1],[89,1],[94,1]]
    print(f' Los 5 productos menos vendidos son los siguientes(ID, N. de Ventas):\n{menosvent}\n')

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

    #Hacermos lista para conocer el numero de busquedas por producto
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
    srchs_pantallas = lista_srchs[32:35]
    srchs_bocinas = lista_srchs[35:36]
    srchs_audifonos = lista_srchs[36:40]
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_process} para cada Id de los procesadores.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_t_video} para cada Id de las tarjetas de video.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_t_madre} para cada Id de las tarjetas madre.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_driv_hd} para cada Id de los discos duros.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_pantallas} para cada Id de las pantallas.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_bocinas} para cada Id de las bocinas.\n')
    print(f'Las menores busquedas por categoria son la siguientes: {srchs_audifonos} para cada Id de los audifonos.\n')

    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_process, reverse=True)} para cada Id de los procesadores.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_t_video, reverse=True)} para cada Id de las tarjetas de video.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_t_madre, reverse=True)} para cada Id de las tarjetas madre.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_driv_hd, reverse=True)} para cada Id de los discos duros.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_pantallas, reverse=True)} para cada Id de las pantallas.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_bocinas, reverse=True)} para cada Id de las bocinas.\n')
    print(f'Las mayores busquedas por categoria son la siguientes: {sorted(srchs_audifonos, reverse=True)} para cada Id de los audifonos.\n')

def ejercicio2():
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
    print(f'{resutltado_ordenado[0:5]}\n')

def ejercicio3():
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



    for key in categorizacion_meses.keys():
        print(key)
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

    print(f' Obtenemos el total de unidades vendidas que corresponde a: \n {suma_venta} unidades.')

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
    print(f' Los ingresos totales corresponden a ${(sum(total_ventas))}.')





def menu():
        login()
        while True:
            print('Que resultado deseas obtener:')
            print('\t1. Obtenga los productos mas vendidos y rezagados.')
            print('\t2. Obtenga las estadísticas de los productos con base en su reseña.')
            print('\t3. Obtenga las estadísiticas generales de ingresos y ventas.')
            print('\t0. Salir')
            seleccion = input('> ')
            if seleccion == '1':
                ejercicio1()
            elif seleccion == '2':
                ejercicio2()
            elif seleccion == '3':
                ejercicio3()
                print('\n')
            elif seleccion == '0':
                exit()
            else:
                print('Opcion invalida!')

menu()
