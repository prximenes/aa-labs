#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prática de Laboratório: Análise de Algoritmos • UNICAP
Missão 2: Decisão vs. Busca (A Diferença de Complexidade entre Saber e Encontrar)
Prof. Pedro Ximenes
"""

import time
import math
import random

def teste_decisao_composto(n, rodadas=10):
    """
    PROBLEMA DE DECISÃO: 'n é composto?' (SIM / NÃO)
    Executa o teste de Miller-Rabin com base em testemunhas estocásticas.
    Retorna True se for composto ('SIM'), ou False se for primo ('NÃO').
    """
    if n < 2:
        return False
    if n in (2, 3):
        return False
    if n % 2 == 0:
        return True

    # Decompor n - 1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Rodadas de testemunhas de Miller-Rabin
    for _ in range(rodadas):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composto = True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composto = False
                break
        if composto:
            return True  # 'SIM', n é composto com 100% de certeza!

    return False  # 'NÃO', n é primo

def busca_fatores(n, limite_tempo=3.0):
    """
    PROBLEMA DE BUSCA: 'Quais são os fatores p e q de n?'
    Algoritmo de divisão por tentativa (Exponencial no número de bits de n).
    Retorna: (p, q, passos, timeout)
    """
    passos = 0
    t0 = time.perf_counter()

    if n % 2 == 0:
        return 2, n // 2, 1, False

    limite = math.isqrt(n)
    d = 3
    while d <= limite:
        passos += 1
        if n % d == 0:
            return d, n // d, passos, False
        d += 2

        # Checagem de segurança a cada 200.000 iterações
        if passos % 200_000 == 0:
            if time.perf_counter() - t0 > limite_tempo:
                return None, None, passos, True

    return None, None, passos, False

def main():
    print("=" * 82)
    print("  MISSÃO 2: DECISÃO VS. BUSCA (SLIDES 22 E 23)")
    print("  'Saber se é Composto' (Decisão)  vs.  'Encontrar os Fatores' (Busca)")
    print("=" * 82)
    print()

    amostras = [
        {
            "descricao": "Número Pequeno (32 bits)",
            "n": 4294049777,
            "fatores_reais": (65521, 65537)
        },
        {
            "descricao": "Número Médio (42 bits)",
            "n": 4398063288167,
            "fatores_reais": (2097143, 2097169)
        },
        {
            "descricao": "Número Grande (54 bits)",
            "n": 4503600298459061,
            "fatores_reais": (67108859, 67108879)
        },
        {
            "descricao": "Número Criptográfico (70 bits)",
            "n": 1180591625390335725871,
            "fatores_reais": (34359738421, 34359738451)
        }
    ]

    print(f"{'Descrição':<30} | {'Valor de n':<24} | {'Decisão (SIM/NÃO)':<18} | {'Busca (p, q)':<20}")
    print("-" * 100)

    for item in amostras:
        n = item["n"]

        # --- 1. DECISÃO ---
        t0 = time.perf_counter()
        eh_composto = teste_decisao_composto(n, rodadas=15)
        t_decisao = time.perf_counter() - t0
        resp_decisao = f"SIM ({t_decisao*1000:6.3f} ms)" if eh_composto else f"NÃO ({t_decisao*1000:6.3f} ms)"

        # --- 2. BUSCA ---
        t0 = time.perf_counter()
        p, q, passos, timeout = busca_fatores(n, limite_tempo=2.0)
        t_busca = time.perf_counter() - t0

        if timeout:
            resp_busca = f"TIMEOUT (> {t_busca:.1f}s)"
        else:
            resp_busca = f"{p}x{q} ({t_busca:.4f}s)"

        print(f"{item['descricao']:<30} | {n:<24} | {resp_decisao:<18} | {resp_busca:<20}")

    print("-" * 100)
    print()
    print("📝 Transcreva os valores medidos para a Tabela 2 e responda às perguntas 4 e 5 à mão no caderno.")
    print("=" * 100)

if __name__ == "__main__":
    main()
