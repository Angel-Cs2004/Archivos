# 12. Se tiene el archivo “Dpto_Provincias.txt”, que contiene la cantidad de provincias de cada
# departamento. El usuario ingresará el nombre de un departamento y el programa debe responder
# cuántas provincias tiene. En caso que el departamento no esté en el archivo se debe indicar con un
# mensaje. La estructura del archivo puede ser:
# Amazonas 7
# Arequipa 8
# Huánuco 9
# Lima 10
# Tacna 4
# …

# def provinces(departament):
#     file=open('Provincias.txt','r')
#     string=file.read().lower().split()
#     if departament in string:
#         print(f'la provincia de {departament} tiene {string[string.index(departament)+1]} provincias')



def provinces(departament): # version sin la funcion index
    file=open('Provincias.txt','r')
    string=file.read().lower().split()
    if departament in string:
        for indice in range(0,len(string)):
            if departament==string[indice]:
                print(f'la provincia de {departament} tiene {string[indice+1]} provincias')
                break

departament=input('Introduzca el departamento: ')
provinces(departament)