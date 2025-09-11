#Dado duas listas, printe todos os valores que aparecerem duplicados nas duas listas
valores1 = [3, 4, 5, 6, 7, 8,]
valores2 = [2, 4, 6, 8, 10]

for lista in valores1:
    if lista == lista in valores2:
     print(lista)
print('\n')

#Dado duas listas, printe umas mesagem dizendo se existe algum elemento em comum entre elas ou não

lista1 = ['Juan', 23, False]
lista2 = ['Larissa', 21, False]

elemento_em_comum = False;

for valor1 in lista1:
   for valor2 in lista2:
      if valor1 == valor2:
         elemento_em_comum = True;
if elemento_em_comum:
   print('As listas {lista1} e {lista2} possuem elementos em comum')
else:
   print('As listas {lista1} e {lista2} não possuem elementos em comum')