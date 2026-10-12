#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prática de Laboratório: Análise de Algoritmos • UNICAP
Missão 1: A Assimetria do RSA (Multiplicação Polinomial vs. Fatoração Exponencial)
Prof. Pedro Ximenes
"""

import time
import math

# Pares de primos (p, q) para simular chaves RSA de tamanhos crescentes
CENARIOS_RSA = [
    {
        "nome": "Chave Pequena (16 bits)",
        "p": 251,
        "q": 257,
        "limite_passos": 10_000_000
    },
    {
        "nome": "Chave Média (32 bits)",
        "p": 65521,
        "q": 65537,
        "limite_passos": 10_000_000
    },
    {
        "nome": "Chave Grande (42 bits)",
        "p": 2097143,
        "q": 2097169,
        "limite_passos": 10_000_000
    },
    {
        "nome": "Chave Desafio (54 bits)",
        "p": 67108859,
        "q": 67108879,
        "limite_passos": 25_000_000
    }
]

def fatorar_busca_exaustiva(n, max_passos=10_000_000):
    """
    Tenta quebrar o RSA encontrando p e q tais que n = p * q.
    Testa divisores ímpares até sqrt(n).
    """
    passos = 0
    if n % 2 == 0:
        return 2, n // 2, 1, False

    limite = math.isqrt(n)
    d = 3
    while d <= limite:
        passos += 1
        if n % d == 0:
            return d, n // d, passos, False
        d += 2

        if passos >= max_passos:
            return None, None, passos, True  # Atingiu timeout pedagógico

    return None, None, passos, False

def main():
    print("=" * 75)
    print("  MISSÃO 1: A ASSIMETRIA CRIPTOGRÁFICA DO RSA")
    print("  Gerar Chave Pública (Multiplicar) vs. Quebrar RSA (Fatorar)")
    print("=" * 75)
    print()

    print(f"{'Cenário':<24} | {'n = p * q':<16} | {'Tempo Mult.':<12} | {'Tempo Fatorar':<13} | {'Passos Busca':<12}")
    print("-" * 88)

    for c in CENARIOS_RSA:
        p, q = c["p"], c["q"]

        # 1. Gerar Chave (Multiplicação): p * q = n
        t0 = time.perf_counter()
        n = p * q
        t_mult = time.perf_counter() - t0

        # 2. Quebrar Chave (Fatoração por Busca): Dado n, achar p e q
        t0 = time.perf_counter()
        fator_p, fator_q, passos, timeout = fatorar_busca_exaustiva(n, c["limite_passos"])
        t_fator = time.perf_counter() - t0

        if timeout:
            tempo_str = f"> {t_fator:.2f}s (PAUSADO)"
            passos_str = f"> {passos:,}*"
        else:
            tempo_str = f"{t_fator:.5f}s"
            passos_str = f"{passos:,}"

        print(f"{c['nome']:<24} | {n:<16} | {t_mult*1000:7.4f} ms  | {tempo_str:<13} | {passos_str:<12}")

    print("-" * 88)
    print("* O Cenário Desafio foi interrompido por limite de passos para não congelar o terminal.")
    print()
    print("📝 Transcreva os valores medidos para a Tabela 1 e responda às perguntas 1, 2 e 3 à mão no caderno.")
    print("=" * 88)

if __name__ == "__main__":
    main()
