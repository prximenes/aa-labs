import time

# Criando uma instância: vetor de 0 a 9.999.999
print("Gerando vetor na memória...")
vetor_gigante = list(range(10000000))
print("Vetor gerado!\n")

def busca(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    return False

# Cenário A: Buscando o número 0 (Está logo no começo)
inicio = time.time()
busca(vetor_gigante, 0)
fim = time.time()
print(f"Tempo Cenário A (Buscando 0): {fim - inicio:.6f} s")

# Cenário B: Buscando o número -1 (Não está na lista, varre tudo)
inicio = time.time()
busca(vetor_gigante, -1)
fim = time.time()
print(f"Tempo Cenário B (Buscando -1): {fim - inicio:.6f} s")