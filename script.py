lista_archivo = ['/home/linti/Escritorio/hobbys/mihobby-santiago.md',
                 '/home/linti/Escritorio/hobbys/mihobby-milagros.md',
                 '/home/linti/Escritorio/hobbys/mihobby-ñapi.md',
                 '/home/linti/Escritorio/hobbys/mihobby-orlando.md',
                 '/home/linti/Escritorio/hobbys/mihobby-saigua.md',
                 '/home/linti/Escritorio/hobbys/mihobby-tute.md',
                 '/home/linti/Escritorio/hobbys/myhobby-tomas.md']

lista_nombres = ['Santiago','Milagros','Ñapi','Orlando','Saigua','Tute','Tomas']
numero = 0
nombres ={}
for archivo in lista_archivo:
    diccionario = {}
    abrir = open(archivo) #abrir el archivo
    texto = abrir.read() #leerlo y guardarlo en una varible string
    abrir.close() #cerrar el archivo
    for linea in texto.splitlines()[2:]:
        palabra = linea.split(':')
        palabra[0]=palabra[0].replace("*","")
        diccionario[palabra[0]] = len(palabra[1])     
    nombres[lista_nombres[numero]] = diccionario
    numero +=1
print(nombres)