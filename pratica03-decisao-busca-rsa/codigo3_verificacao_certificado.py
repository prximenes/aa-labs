#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prática de Laboratório: Análise de Algoritmos • UNICAP
Missão 3: Encontrar vs. Verificar (A Facilidade de Checar um Certificado)
Prof. Pedro Ximenes
"""

import time

def verificar_certificado(n, candidato_p):
    """
    Verifica se candidato_p é um divisor não-trivial de n.
    """
    t0 = time.perf_counter()
    eh_valido = (1 < candidato_p < n) and (n % candidato_p == 0)
    q = (n // candidato_p) if eh_valido else None
    t_gasto = time.perf_counter() - t0
    return eh_valido, q, t_gasto

def main():
    print("=" * 82)
    print("  MISSÃO 3: TESTE DE VALIDADE DE CERTIFICADOS")
    print("  Verificando se um candidato proposto realmente divide o número público n")
    print("=" * 82)
    print()

    # Um número RSA de 70 bits onde a busca demoraria dias/semanas
    n = 1180591625390335725871
    print(f"Número RSA Público: n = {n} (~70 bits)")
    print("Testando candidatos fornecidos como supostos fatores:")
    print("-" * 82)

    testes = [
        ("Certificado A", 34359738421),
        ("Certificado B", 34359738423),
        ("Certificado C", 12345678901)
    ]

    for label, cand in testes:
        valido, outro_fator, tempo = verificar_certificado(n, cand)
        status = f"✅ VÁLIDO! (outro fator = {outro_fator})" if valido else "❌ INVÁLIDO (não divide n)"
        print(f"{label:<20} | Candidato p = {cand:<14} | {status:<32} | Tempo: {tempo*1e6:.2f} µs")

    print("-" * 82)
    print()
    print("📝 Responda às perguntas 6 e 7 à mão no caderno explicando a diferença de complexidade observada.")
    print("=" * 82)

if __name__ == "__main__":
    main()
