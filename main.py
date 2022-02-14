from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


"""
Login
credenciales:

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




#-------------------------------------------------------------------------------------------------------
# Lista productos








print('No existen errores en el código')










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

resutltado_ordenado = sorted(listaResultado,key= lambda x : x[1][2],reverse=False)

print(resutltado_ordenado)
