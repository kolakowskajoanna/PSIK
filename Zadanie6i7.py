from audioop import reverse

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
lista2 = lista[5:10]
lista = lista[0:5]
print(lista)
print(lista2)
lista.extend(lista2)
lista.insert(0,0)
print(lista)
lista3=lista
lista3.reverse()
print(lista3)