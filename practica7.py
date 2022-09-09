'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Brian Avalos Sanchez
Continuación de la práctica 6
'''
import random
import bcrypt

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
'''

def regresa_conjunto_estudiantes():
    estudiantes = set()
    tupla_estudiante = ()
    with open("estudiantes.prn") as arch_estudiantes:
        for linea in arch_estudiantes:
            control = linea[0:8]
            nombre = linea[8:-1]
            estudiantes.add((control,nombre))
    arch_estudiantes.close()
    return estudiantes


'''
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }

4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]



5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - cifrar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada
'''

def generar_letra_mayuscula(): #Regresa una letra desde la A ... Z
    return chr(random.randint(65,90))

def generar_letra_minuscula(): #Regresa una letra desde la a ... z
    return chr(random.randint(97,122))

def generar_numeros(): #Regresa un numero aleatorio entre 0 ... 9
    return chr(random.randint(48,57))

def generar_caracteres_especiales(): #Regresa un caracter aleatorio
    lista_caracteres = ['@','#','¢','%','&','/','?','¿']
    return lista_caracteres[random.randint(0,7)]

def generar_contraseña():
    clave = ""
    for i in range(0,10):
        numero=random.randint(1,5)

        if numero == 1:
            clave = clave + generar_letra_mayuscula()
        elif numero == 2:
            clave = clave + generar_letra_minuscula()
        elif numero == 3:
            clave = clave + generar_caracteres_especiales()
        elif numero >=4 and numero <=5:
            clave = clave + generar_numeros()
    return clave

print(generar_contraseña())

#cifrar la contraseña con bcrypt
def cifrar_contrasena(contrasena):
    sal = bcrypt.gensalt() #default tiene un valor de 12
    contrasena_cifrada = bcrypt.hashpw(contrasena.encode('utf-8'),sal)
    return contrasena_cifrada

clave = generar_contraseña()
print(clave,cifrar_contrasena(clave))
'''
#Generar el archivo de usuarios
def generar_archivo_usuarios():
    #obtener la lista de estudiantes
    estudiantes = regresa_conjunto_estudiantes()
    print("estudiantes")
    print(estudiantes)
    usuarios = open("usuarios.txt", "w")
    contador = 1
    for est in estudiantes:
        c,n = est
        clave = generar_contraseña()
        clave_cifrada = cifrar_contrasena(clave)
        registro = c + " "+ clave + " " + str(clave_cifrada, 'utf-8') + "\n"
        usuarios.write(registro)
        contador += 1
        print(contador)
    print("archivo generado")

generar_archivo_usuarios()
'''
'''
print(bcrypt.checkpw("63T72Ml3b1".encode('utf-8'),"$2b$12$bzy7EMXDruCzYxAk5eZXB./W2ySqLqjfOlURMz.GDd6uMbgHDzRY6"))

'''
def autenticar_usuario(user, contrasena):
    res = {}
    if user != "":
        usuarios = open("usuarios.txt", mode="r")
        alum = usuarios.read().split("\n")

        for alumno in alum:
            separado = alumno.split(" ")
            if len(separado) >= 0:
                if user == separado[0]:
                    if bcrypt.checkpw(contrasena.encode('utf-8'), separado[2].encode('utf-8')):
                        res = {"Bandera": True, "Usuario": separado[0], "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"}
                    else:
                        res = {"Bandera": False, "Usuario": separado[0], "Mensaje": "Contraseña incorrecta"}
                    break
    if len(res) == 0:
        res = {"Bandera": False, "Usuario": "", "Mensaje": "No existe el Usuario"}

    print(res)

autenticar_usuario('18420470','lJAT1mfT¢2')#correcto

'''
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }
   ó
   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }
   ó
    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }
'''
