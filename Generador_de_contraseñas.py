#import requests
import string
import random

print('Este programa te ayudara a generar una contraseña segura')
eleccion = input('Desea generarla de manera automatica? si/no ')

if (eleccion == 'si'):
    longitud = 16

    caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    print('Su contraseña generada es:\n' + contraseña)

    # Envía la contraseña a la página web como un parámetro GET
    # respuesta = requests.get ("https://www.security.org/how-secure-is-my-password/", 
    #                         params = {"password": contraseña})
    # # Analiza la respuesta para obtener el tiempo estimado de crackeo
    # tiempo = analizar_respuesta (respuesta)
    # # Imprime el resultado
    # print (f"La contraseña tardaría {tiempo} en ser crackeada")

elif (eleccion == 'no'):
    longitud = int(input('Ingrese tamaño que quiere que tenga su contraseña de contraseña: '))

    eleccion_de_caracteres = input('Desea que ademas de numeros poseea letras? si/no ')
    if (eleccion_de_caracteres == 'si'):

        caracteres = string.ascii_letters + string.digits
    
    else:
        caracteres = string.digits
        
        
    eleccion_de_caracteres_especiales = input('Desea que ademas poseea simbolos? si/no ')
    if (eleccion_de_caracteres_especiales == 'si'):
        caracteres =  caracteres + string.punctuation
    
    else:
        caracteres = caracteres
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    print('Su contraseña generada es:\n' + contraseña)
    
    
