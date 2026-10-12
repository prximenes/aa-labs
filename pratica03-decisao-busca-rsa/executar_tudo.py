#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prática de Laboratório: Análise de Algoritmos • UNICAP
Script Integrador: Execução Completa das 3 Missões
Prof. Pedro Ximenes
"""

import os
import sys
import subprocess

DIR_ATUAL = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    ("Missão 1: A Assimetria do RSA (Multiplicação vs. Fatoração)", "codigo1_rsa_assimetria.py"),
    ("Missão 2: Decisão vs. Busca (Miller-Rabin vs. Divisão)", "codigo2_decisao_vs_busca.py"),
    ("Missão 3: Encontrar vs. Verificar (Certificados Polinomiais)", "codigo3_verificacao_certificado.py")
]

def main():
    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║     UNICAP • ANÁLISE DE ALGORITMOS • PROF. PEDRO XIMENES               ║")
    print("║     PRÁTICA DE LABORATÓRIO: DECISÃO VS. BUSCA & DIFICULDADE DO RSA      ║")
    print("╚════════════════════════════════════════════════════════════════════════╝")
    print()

    for i, (titulo, script_nome) in enumerate(SCRIPTS, 1):
        caminho_script = os.path.join(DIR_ATUAL, script_nome)
        print(f"\n[{i}/3] EXECUTANDO: {titulo.upper()}...\n")
        resultado = subprocess.run([sys.executable, caminho_script])
        if resultado.returncode != 0:
            print(f"Erro ao executar {script_nome}")
            break
        print("\n" + "="*80)

    print("\n🎉 Todas as missões foram executadas com sucesso!")
    print("📝 Transcreva os dados medidos e responda a todas as perguntas reflexivas À MÃO NO SEU CADERNO.")

if __name__ == "__main__":
    main()
