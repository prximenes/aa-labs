import time

def primo_linear(n):
    """Verifica primalidade testando de 2 ate n-1: O(n)"""
    passos = 0
    if n <= 1:
        return False, passos
    for i in range(2, n):
        passos += 1
        if n % i == 0:
            return False, passos
    return True, passos

def primo_raiz(n):
    """Verifica primalidade testando com i * i <= n: O(sqrt(n))"""
    passos = 0
    if n <= 1:
        return False, passos
    i = 2
    while i * i <= n:
        passos += 1
        if n % i == 0:
            return False, passos
        i += 1
    return True, passos

# Primos grandes conhecidos (Garantem o PIOR CASO de ambos os algoritmos)
testes_primos = [100003, 1000033, 10000019]

print("=" * 68)
print("MISSÃO 1: Teste de Primalidade - O(n) vs O(sqrt(n))")
print("=" * 68)
print(f"{'n':<12} | {'Algoritmo':<15} | {'Operações':<12} | {'Tempo (s)':<12}")
print("-" * 68)

for n in testes_primos:
    # Teste O(n)
    t0 = time.time()
    _, passos_lin = primo_linear(n)
    t1 = time.time()
    tempo_lin = t1 - t0
    print(f"{n:<12} | {'Linear O(n)':<15} | {passos_lin:<12} | {tempo_lin:.6f} s")

    # Teste O(sqrt(n))
    t0 = time.time()
    _, passos_rz = primo_raiz(n)
    t1 = time.time()
    tempo_rz = t1 - t0
    print(f"{n:<12} | {'Raiz O(sqrt(n))':<15} | {passos_rz:<12} | {tempo_rz:.6f} s")
    print("-" * 68)
