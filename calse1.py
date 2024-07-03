archivo = open('C:/Users/Angelo/Documents/block de notas/perro.txt', 'r+') # Modo escritura (sobreescribe)
print(archivo.read())
archivo.write(" pero aun si te seguire sonando \n")
archivo.close()
