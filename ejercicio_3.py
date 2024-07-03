#3. Imprimir el contenido de un archivo línea por línea.
def leer(archivo):
    file=open(archivo,"r")
    count=1
    for i in file:
        print(f'Linea {count}: ')
        print(i,end="")
        count+=1
archivo=input("introduzca la direccion del archivo: ")
leer(archivo)