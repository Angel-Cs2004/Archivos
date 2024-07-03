# 7. Contar el número de líneas de un archivo.
archive=input('introduzca: ')
file=open(archive,"r")
number_line=0
for line in file:
    number_line+=1
file.close()
print(f'el numero de lineas es: {number_line}')