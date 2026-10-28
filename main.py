import librerias as lb
import os

#Variables
Activo = True # bandera que controla el bucle
Archivo_cargado = False #bandera que indica cuando el archivo ya este cargado

#Bucle que mantiene funcionando el codigo
while Activo:
    try:
        print("""    Menu     
1) Cargar Archivo
2) Búsqueda Exacta 
3) Búsqueda Simple 
4) Búsqueda por Prefijo 
5) Estadísticas 
6) Buscar Palabra NoX 
7) Análisis Comparativo 

0) Salir""")
        
        print("")
        elec = int(input("Eleccion: "))

        if elec <0 or elec >7:
            print("Error, numero fuera de rango.")

        elif elec == 0:
            sali = input("Seguro de querer salir(s/n):").lower()
            if sali == "s":
                print("Saliendo")
                Activo = False

        elif elec != 1 and Archivo_cargado:
            match elec:
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
        elif elec != 1 and not(Archivo_cargado):
            print("No puede acceder a esta funcion hasta que el archivo sea cargado.")
            enter = input("""
Presione enter para continuar: """)
        else:
            if Archivo_cargado:
                des = input("ya tienes un archivo cargado, deseas cambiarlo? (s/n): ").lower()

                if des != "s":
                    continue

            nuevo = lb.Cargar_Archivo() #Varible alamacena el retorno del algoritmo

            if nuevo is not None: #si el retorno no es None el archivo fue cargado con exito
                palabras = nuevo # aqui almacenamos una lista(tupla) que tendra cada palabra
                Archivo_cargado = True 
                print("Archivo cargado con Exito")
                print(f"total de palabras {len(palabras)}") #mostramos la cantidad de palabras 
                enter = input("""
Presione enter para continuar: """)
                
            else:
                print("error, Archivo no fue cargado.")
                enter = input("""
Presione enter para continuar: """)

        
        
    except Exception as e:
        print(e)