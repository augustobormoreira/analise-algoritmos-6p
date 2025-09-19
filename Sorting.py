import random
import time

# Insertion Sort
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n): 
        key = lista[i] 
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j] 
            j -= 1
        lista[j+1] = key  


# Bubble Sort
def bubble_sort(lista):
  n = len(lista)
  for i in range(n-1):
    for j in range(n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista;


# Selection Sort
def selection_sort(lista):
   tamanho = len(lista)
   for ind in range(tamanho):
      min_index = ind
      for j in range(ind + 1, tamanho):
          if lista[j] < lista[min_index]:
            min_index = j
      (lista[ind], lista[min_index]) = (lista[min_index], lista[ind])
    
   return lista

# Merge Sort
def merge(lista, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = lista[l + i]

    for j in range(0, n2):
        R[j] = lista[m + 1 + j]

    i = 0    
    j = 0     
    k = l     

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        lista[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lista[k] = R[j]
        j += 1
        k += 1

def merge_sort(lista, list_esq, lista_dir):
    if list_esq < lista_dir:

        meio = list_esq+(lista_dir-list_esq)//2

        merge_sort(lista, list_esq, m)
        merge_sort(lista, meio+1, lista_dir)
        merge(lista, list_esq, meio, lista_dir)


# Quick Sort
def partition(lista, menor, maior):

    pivot = lista[maior]

   
    i = menor - 1
    for j in range(menor, maior):
        if lista[j] <= pivot:
            i = i + 1
            (lista[i], lista[j]) = (lista[j], lista[i])

    (lista[i + 1], lista[maior]) = (lista[maior], lista[i + 1])
    return i + 1


def quickSort(lista, menor, maior):

    if menor < maior:
        pi = partition(lista, menor, maior)
        quickSort(lista, menor, pi - 1)
        quickSort(lista, pi + 1, maior)
    
    return lista

#Função para criar uma lista desordenada preenchida por valores randômicos

def lista_desordenada(tamanho):
  return [random.randint(0, tamanho) for _ in range(tamanho)]


#Lista contendo os tamanhos das entradas
tamanhos = [10, 100, 1000, 5000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]


# Para cada tamanho, cria uma lista daquele tamanho e executa o algoritmo que quiser
for tamanho in tamanhos:
  print(f"tamanho da lista: {tamanho}")
  lista = lista_desordenada(tamanho)


  comeco = time.time()

  #bubble_sort(lista)
  #insertion_sort(lista)
  #selection_sort(lista)
  #quickSort(lista, 0, len(lista)-1)
  merge_sort(lista, 0, len(lista)-1)
  fim = time.time()
  tempo_tot = fim - comeco

  tempo_total = fim - comeco
  print(f"Tempo total: {tempo_tot:.6f} segundos")
  print("-" * 20)
