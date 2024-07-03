# 10. Contar cuantas veces se repite una palabra en un archivo.
def repeat():
    file=open('archivo.txt','r')
    list=[]
    for line in file:
        string=line.replace('\n',' ') #remplazo valores de \n por " " 
        list_word=string.split() # el split tranformo en lista a la cadena(line) , con los delimitadores " " 
        print(type(list_word))
        list_word=[word for word in list_word if word] # aqui utlize thi com...
        list+=list_word
    
    for word in set(list): #utilizo la funcion set() para evitar los repetidos
        repeat_word=0
        for word_1 in list:
            if word==word_1:
                repeat_word+=1
        print(f'{word}: {repeat_word} ')

print(repeat())


        # for word in list_word:
        #     cant_pal=-1
        #     for i in list_word:
        #        if word==i:
        #             cant_pal+=1

