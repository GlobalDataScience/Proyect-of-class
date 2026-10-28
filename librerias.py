import os
def Cargar_Archivo():

    dec = input("ADVERTENCIA: para poder cargar el archivo, este debe estar en la carpeta Archivos. Esta ahi (s/n)? :").lower()
    if dec != "s":
        print("ingrese el archivo a la carpeta (Archivos) y luego vuelva a prender el programa.")
        print("")
        return None

    nombre = input("ingrese el nombre del archivo .txt: ").strip()
    if not nombre.lower().endswith(".txt"):
        print("Error, el archivo debe terminar en un .txt")
        return None
    
    ruta = os.path.join(os.path.dirname(__file__), "Archivos", nombre)
    nuevas_palabras = []

    try:
        with open(ruta,"r", encoding="utf-8") as archivo:
            for num_lista, linea in enumerate(archivo,1):

                for palabra in linea.split():

                    nuevas_palabras.append((palabra,num_lista))

        if len(nuevas_palabras) == 0:
            print("Archivo vacio o no contiene palabras")
            return None

        return nuevas_palabras

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")

    except PermissionError:
        print("Error: no tiene permisos para leer el archivo.")

    except UnicodeDecodeError:
        print("Error: no se pudo leer la codificación del archivo.")

    except OSError:
        print("Error: no se pudo abrir el archivo.")

    return None

    

    
def Busqueda():
    pass

def Busqueda_simple():
    pass

def Busqueda_prefijo():
    pass

def Estadisticas():
    pass

def palabra_numero():
    pass

def Comparacion():
    pass
