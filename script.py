lista_archivo = ['/home/linti/Escritorio/hobbys/mihobby-santiago.md', 
                 '/home/linti/Escritorio/hobbys/mihobby-milagros.md',
                 '/home/linti/Escritorio/hobbys/mihobby-ñapi.md',
                 '/home/linti/Escritorio/hobbys/mihobby-orlando.md',
                 '/home/linti/Escritorio/hobbys/mihobby-saigua.md',
                 '/home/linti/Escritorio/hobbys/mihobby-tute.md',
                 '/home/linti/Escritorio/hobbys/myhobby-tomas.md']

                 #  ↑ ↑ ↑ ↑ ↑ 
                 #  Guarda dentro de una lista las ubicaciones de los archivos MarkDown a utilizar.
                 
  
lista_nombres = ['Santiago','Milagros','Ñapi','Orlando','Saigua','Tute','Tomas'] # Crea una lista donde aparece los nombres de cada quien es su archivo Markdown
numero = 0 # Comienza la lista desde 0, empezando por el elemento 'Santiago'
nombres ={} # Crea un diccionario
for archivo in lista_archivo: # Comienza realizando un FOR en donde recorre la lista "lista_archivo" y lo guarda en "archivo"
    diccionario = {} # Crea un diccionario
    abrir = open(archivo) # Abre los archivos
    texto = abrir.read() # Lee y guarda en una varible string el contenido de los Markdown
    abrir.close() # Cierra los archivos
    for linea in texto.splitlines()[2:]: # Crea otro FOR en donde comienza a dividir el contenido del Markdown a partir de la linea 2 del documento de texto
        palabra = linea.split(':') # Divide el contenido(Palabra clave y Respuesta) utilizando como medio ":" como separador
        palabra[0]=palabra[0].replace("*","") # Reemplaza el asterisco antes de la palabra clave por un espacion en blanco
        diccionario[palabra[0]] = len(palabra[1]) # Guarda en "diccionario" como primer elemento de la lista, la palabra clave y como segundo elemento, la longitud de la respuesta
    nombres[lista_nombres[numero]] = diccionario # Guarda en "nombres" todo los valores guardados en "diccionario" y recorre la lista "lista_nombres" comenzando por 0
    numero +=1 # Va sumando +1 a la lista "lista_nombres"   
print(nombres) # Imprime todo el contenido de la variable "nombres", el creador de cada markdown, la palabra clave y la longitud de la respuesta
