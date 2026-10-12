import sys

# Aumenta limite de recursao se necessario
sys.setrecursionlimit(5000)

def busca_binaria_instrumentada(n, nivel=1):
    """
    Simula Busca Binaria recursiva:
    T(n) = T(n/2) + O(1)
    Parametros: a = 1, b = 2, f(n) = O(1) -> log_b(a) = log_2(1) = 0 -> Caso 2: Theta(log n)
    """
    if n <= 1:
        return 1, nivel  # (total de chamadas, profundidade maxima)
    
    chamadas, prof = busca_binaria_instrumentada(n // 2, nivel + 1)
    return chamadas + 1, prof

def divisao_dupla_instrumentada(n, nivel=1):
    """
    Simula divisao com 2 subproblemas:
    T(n) = 2 T(n/2) + O(1)
    Parametros: a = 2, b = 2, f(n) = O(1) -> log_b(a) = log_2(2) = 1 -> Caso 1: Theta(n)
    """
    if n <= 1:
        return 1, nivel
    
    c1, p1 = divisao_dupla_instrumentada(n // 2, nivel + 1)
    c2, p2 = divisao_dupla_instrumentada(n // 2, nivel + 1)
    return c1 + c2 + 1, max(p1, p2)

tamanhos = [1024, 32768, 1048576]

print("=" * 76)
print("MISSÃO 4: Árvore da Recursão e Teorema Mestre")
print("=" * 76)
print(f"{'n':<12} | {'Algoritmo':<22} | {'Profundidade (Pilha)':<20} | {'Total Chamadas':<15}")
print("-" * 76)

for n in tamanhos:
    chamadas_bb, prof_bb = busca_binaria_instrumentada(n)
    print(f"{n:<12} | {'Busca Binária (a=1)':<22} | {prof_bb:<20} | {chamadas_bb:<15}")
    
    # Para n muito grande, a divisao dupla faz 2*n chamadas; rodamos para os dois primeiros
    if n <= 32768:
        chamadas_dup, prof_dup = divisao_dupla_instrumentada(n)
        print(f"{'':<12} | {'Divisão Dupla (a=2)':<22} | {prof_dup:<20} | {chamadas_dup:<15}")
    else:
        # Previsao teorica exata: 2^(log2(n)+1) - 1
        print(f"{'':<12} | {'Divisão Dupla (a=2)':<22} | {prof_bb:<20} | {2*n - 1:<15} (calculado)")
    print("-" * 76)
