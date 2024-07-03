# 13. Leer del archivo “Votos.txt” los votos para cada uno de los tres candidatos. El programa debe escribir
# en otro archivo la cantidad total de votos que obtuvo cada uno. Por ejemplo, si el contenido del archivo
# “Votos.txt” es:
# 1 2 1 1 2 1 3
# El otro archivo deberá contener:
# Candidato 1: 4 votos
# Candidato 2: 2 votos
# Candidato 3: 1 votos
candidate=int(input('Cuantos candidatos participaron: '))
file=open("votos.txt",'r')
string=file.read().replace('',' ').split()
for number in range(1,candidate+1):
    count=0
    for number_2 in string:
        if number==int(number_2):
            count+=1
    print(f'Candidato {number}: {count}')