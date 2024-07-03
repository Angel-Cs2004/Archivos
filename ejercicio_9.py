# 9. Contar el número de palabras de un archivo.
def number_word():
    file=open("archivo.txt",'r')
    number_word=0
    string=''
    for line in file:
        for caracter in line:
            if caracter!=' ' and caracter!="\n":
                string+=caracter
            else:
                number_word+=1
                string=''
        if string:
            number_word+=1

    return number_word
print(f"la cantidad de palabras es: {number_word()}")