# 11. Buscar una palabra en el archivo y reemplazarla por otra
def replace(word_search,word_replace):
    file=open('archivo.txt','r')
    string=file.read().replace(word_search,word_replace)
    file= open('archivo.txt','w')
    file.write(string)
    file.close

    return string

word_search=input('Que palabra gustas remplazar?: ')
word_replace=input('Por que palabra desa remplazarlo?: ')
print(replace(word_search,word_replace))