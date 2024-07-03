# 14. Invertir el contenido de un archivo letra a letras
file=open('texto.txt','r')
string=file.read().replace('\n',' ')
reverse_string=''
for caracter in string[-1:-(len(string)+1):-1]:
    reverse_string+=caracter
print(reverse_string)
string=reverse_string
file=open('texto.txt','w')
file.write(string) 
file.close() 
