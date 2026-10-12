import time

# Definicao de uma Lista Simplesmente Encadeada didatica
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, valor):
        """Operacao O(1): cria no e ajusta ponteiro da cabeca"""
        novo = Nodo(valor)
        novo.proximo = self.head
        self.head = novo

def teste_vetor_dinamico(n):
    """Insercao de n elementos sempre no indice 0 de um vetor contiguo"""
    vetor = []
    t0 = time.time()
    for x in range(n):
        vetor.insert(0, x)  # Forca o deslocamento de todos os elementos existentes
    t1 = time.time()
    return t1 - t0

def teste_lista_encadeada(n):
    """Insercao de n elementos sempre no inicio de uma lista encadeada"""
    lista = ListaEncadeada()
    t0 = time.time()
    for x in range(n):
        lista.inserir_no_inicio(x)  # Apenas atualizacao de ponteiros
    t1 = time.time()
    return t1 - t0

tamanhos = [10000, 30000, 60000]

print("=" * 72)
print("MISSÃO 3: Inserção no Início - Vetor vs Lista Encadeada")
print("=" * 72)
print(f"{'N inserções':<14} | {'Vetor list.insert(0)':<25} | {'Lista Encadeada (O(1))':<25}")
print("-" * 72)

for n in tamanhos:
    tempo_vetor = teste_vetor_dinamico(n)
    tempo_encadeada = teste_lista_encadeada(n)
    print(f"{n:<14} | {tempo_vetor:.5f} s (Quadratica)    | {tempo_encadeada:.5f} s (Linear)")
print("-" * 72)
