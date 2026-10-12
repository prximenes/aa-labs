import time
import random

def insertion_sort(arr_original):
    arr = list(arr_original)
    n = len(arr)
    comparacoes = 0
    deslocamentos = 0
    
    t0 = time.time()
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                deslocamentos += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
    t1 = time.time()
    return comparacoes, deslocamentos, t1 - t0

def selection_sort(arr_original):
    arr = list(arr_original)
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    t0 = time.time()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    t1 = time.time()
    return comparacoes, trocas, t1 - t0

# Configuracao dos testes (n = 2000 elementos)
N = 2000
random.seed(42)

cenarios = {
    "1. Já Ordenado": list(range(N)),
    "2. Invertido": list(range(N, 0, -1)),
    "3. Aleatório": random.sample(range(N * 5), N)
}

print("=" * 78)
print(f"MISSÃO 2: Ordenação - Insertion Sort vs Selection Sort (N = {N})")
print("=" * 78)
print(f"{'Cenário':<18} | {'Algoritmo':<15} | {'Comparações':<13} | {'Trocas/Movs':<13} | {'Tempo (s)':<10}")
print("-" * 78)

for nome_cenario, dados in cenarios.items():
    # Insertion Sort
    comp_ins, mov_ins, tempo_ins = insertion_sort(dados)
    print(f"{nome_cenario:<18} | {'Insertion Sort':<15} | {comp_ins:<13} | {mov_ins:<13} | {tempo_ins:.5f} s")
    
    # Selection Sort
    comp_sel, troc_sel, tempo_sel = selection_sort(dados)
    print(f"{'':<18} | {'Selection Sort':<15} | {comp_sel:<13} | {troc_sel:<13} | {tempo_sel:.5f} s")
    print("-" * 78)
