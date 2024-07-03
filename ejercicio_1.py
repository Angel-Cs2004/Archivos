def escritura(enunciado):
    archivo=open('archivo.txt',"a+")
    archivo.write(enunciado + "\n")
    archivo=open('archivo.txt',"r")
    print(archivo.read())
    archivo.close()
enunciado=input('ingrese lo que desea poner en el archivo: ')
print('Lo que se escribio en el archivo')
escritura(enunciado)