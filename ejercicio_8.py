# 8. Contar el número de caracteres que hay en un archivo.
archive=input('introduce la direccion: ')
registry=open(archive,'r')
number_line=0
number=1
for line in registry:
    number_line+=1

registry.seek(0)

contador_line=0
for line in registry:
    contador_line+=1
    print(f'Linea {contador_line}')
    numb_caracter=0
    for caracter in line:
        numb_caracter+=1
    if contador_line<number_line:
        print(numb_caracter-1)
    else:
        print(numb_caracter)
