# 15. Invertir el contenido de cada palabra del archivo “FileX.txt”.
# Este es quedaría así: etsE se
# un ejemplo nu olpmeje

file=open('archivo.txt','r')
c=0
todo=''
for line in file:   # por cada line se impreme la linea, pero tambien el "\n"
    pal_count=''
    for caracter in line: #yo angelo\n
        if caracter!=' ' and caracter!="\n":
            pal_count+=caracter #yo [0,1] o [-1,-2]
        else:
            if caracter=="\n":
                todo+=pal_count[-1:-(len(pal_count)+1):-1]+"\n"  #yo perrrrro    
                pal_count=''
            else:
                 todo+=pal_count[-1:-(len(pal_count)+1):-1]+" "  #yo perrrrro    
                 pal_count=''
    if pal_count!='':
       todo+=pal_count[-1:-(len(pal_count)+1):-1]
file=open('archivo.txt','w+')
final=file.write(todo)
print(todo)
file.close()