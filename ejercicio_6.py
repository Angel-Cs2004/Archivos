# 6. Leer cadenas desde teclado y copiarlas en un archivo, el programa debe detenerse cuando se ingresa
# una línea en blanco.

file = open('archivo.txt', 'a+')
string = input('Ingrese cadena: ')
while string != "":
    file.write(string + "\n")
    string = input('Ingrese cadena: ')
file.close()
file= open('archivo.txt','r')
print(file.read())
