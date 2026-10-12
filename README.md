# 🧪 Laboratórios de Análise de Algoritmos • UNICAP

> **Disciplina:** Análise de Algoritmos  
> **Professor:** Pedro Ximenes  
> **Instituição:** Universidade Católica de Pernambuco (UNICAP) • Semestre 2026.2  
> **Portal da Disciplina:** [pedrorafael.dev/courses.html](https://pedrorafael.dev/courses.html)

---

## 📌 Visão Geral

Este repositório público reúne todos os **roteiros práticos de laboratório** e **códigos-fonte em Python** da disciplina de **Análise de Algoritmos**. As atividades foram desenhadas para fornecer comprovação empírica direta dos conceitos assintóticos e teóricos apresentados nas aulas teóricas.

---

## ⚠️ Regra Geral de Entrega Obrigatória (Manuscrita)

> ✍️ **IMPORTANTE -- LEIA ANTES DE COMEÇAR:**
> - As conclusões, justificativas conceituais e respostas de todas as práticas devem ser **OBRIGATORIAMENTE redigidas À MÃO NO CADERNO** (ou em folha de papel pautada individual/dupla entregue ao professor).
> - **NÃO serão aceitas entregas digitadas** (Word, Google Docs, PDF ou texto copiado), de modo a garantir o raciocínio analítico autêntico e **impedir respostas geradas automaticamente por ferramentas de Inteligência Artificial**.
> - Cada aluno/dupla deve transcrever para o caderno as tabelas preenchidas com os tempos medidos e fundamentar as respostas com suas próprias palavras para visto do professor ao término da aula.

---

## 📂 Práticas Disponíveis

### 1. [Prática 01: A Corrida Assintótica](./pratica01-corrida-assintotica/)
- **Tema:** Comportamento assintótico empírico ($O(n)$ vs $O(n^2)$).
- **Conteúdo:** Execução e cronometragem de loops aninhados e medição da explosão quadrática.
- 📄 Roteiro: [`pratica1.pdf`](./pratica01-corrida-assintotica/pratica1.pdf)
- 🐍 Códigos: `codigo1.py`, `codigo2.py`, `codigo3.py`

### 2. [Prática 02: Primalidade e Ordenação](./pratica02-ordenacao-primalidade/)
- **Tema:** Teste de primalidade ingênuo vs otimizado ($O(n)$ vs $O(\sqrt{n})$) e ordenação por comparação (Insertion Sort vs Selection Sort).
- **Conteúdo:** Contagem de operações primitivas (comparações e trocas) sobre vetores ordenados, invertidos e aleatórios.
- 📄 Roteiro: [`pratica2.pdf`](./pratica02-ordenacao-primalidade/pratica2.pdf)
- 🐍 Códigos: `codigo1.py`, `codigo2.py`, `codigo3.py`, `codigo4.py`, `executar_tudo.py`

### 3. [Prática 03: Decisão vs. Busca & Dificuldade do RSA](./pratica03-decisao-busca-rsa/)
- **Tema:** [Aula 7: Introdução a Problemas P (Slides 22 a 25)](https://pedrorafael.dev/courses/analise-de-algoritmos/aula7-intro-problemas-p/index.html#22).
- **Conteúdo:**
  - **Missão 1:** A Assimetria do RSA (Multiplicação em frações de microssegundo vs Fatoração com timeout exponencial).
  - **Missão 2:** O Paradoxo de Decisão vs. Busca (Miller-Rabin decide que $n$ é composto em $< 0{,}03$ ms sem conhecer nenhum fator, enquanto a busca exaustiva falha).
  - **Missão 3:** Verificação instantânea de certificados candidatos (ponte para a Classe NP).
- 📄 Roteiro: [`pratica_rsa_decisao_busca.pdf`](./pratica03-decisao-busca-rsa/pratica_rsa_decisao_busca.pdf)
- 🐍 Códigos: `codigo1_rsa_assimetria.py`, `codigo2_decisao_vs_busca.py`, `codigo3_verificacao_certificado.py`, `executar_tudo.py`

---

## 💻 Como Clonar e Executar

```bash
# Clone o repositório
git clone https://github.com/prximenes/aa-labs.git
cd aa-labs

# Entre na pasta da prática desejada:
cd pratica03-decisao-busca-rsa

# Execute o script unificado:
python3 executar_tudo.py
```

### Compilador Online (Sem Instalação)
Se estiver em computadores sem Python instalado, copie o código do arquivo desejado e execute no [Online Python](https://www.online-python.com/).

---

## 🌐 Recursos Adicionais
- 📊 [Simulador Gráfico: Polinomial vs. Exponencial](https://pedrorafael.dev/courses/analise-de-algoritmos/polinomial-vs-exponencial/index.html)
- 📑 [Visualizador de Slides da Aula 7](https://pedrorafael.dev/courses/analise-de-algoritmos/aula7-intro-problemas-p/index.html)
