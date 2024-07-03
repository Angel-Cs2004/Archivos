# 4. Copiar un archivo en otro, reemplazando los espacios en blanco por el caracter ' * '
def remplazo(archive):
    with open(archive,"r") as file:
        for line in file:
            new_line=''
            for index in range(0,len(line)):
                if line[index]==" ":
                   new_line+="*"
                else:
                    new_line+=line[index]
            print(new_line, end='')

archive=input("introduzca la direccion del archivo: ")
remplazo(archive)

