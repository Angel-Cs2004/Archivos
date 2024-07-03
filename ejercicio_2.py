def leer(archivo):
   file=open(archivo ,"r")
   print(file.read())
archivo=input("introduzca la direccion del archivo: ")
leer(archivo)
