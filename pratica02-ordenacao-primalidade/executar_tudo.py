import sys
import subprocess

def main():
    while True:
        print("\n" + "=" * 60)
        print("PRÁTICA DE LABORATÓRIO 02")
        print("=" * 60)
        print("1 - Missão 1: Primalidade O(n) vs O(sqrt(n))")
        print("2 - Missão 2: Duelo Insertion Sort vs Selection Sort")
        print("3 - Missão 3: Custo de Inserção (Vetor vs Lista Encadeada)")
        print("4 - Missão 4: Recursão e Teorema Mestre")
        print("5 - Executar TODAS as missões em sequência")
        print("0 - Sair")
        print("=" * 60)
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            subprocess.run([sys.executable, "codigo1.py"])
        elif escolha == '2':
            subprocess.run([sys.executable, "codigo2.py"])
        elif escolha == '3':
            subprocess.run([sys.executable, "codigo3.py"])
        elif escolha == '4':
            subprocess.run([sys.executable, "codigo4.py"])
        elif escolha == '5':
            subprocess.run([sys.executable, "codigo1.py"])
            print("\n")
            subprocess.run([sys.executable, "codigo2.py"])
            print("\n")
            subprocess.run([sys.executable, "codigo3.py"])
            print("\n")
            subprocess.run([sys.executable, "codigo4.py"])
        elif escolha == '0':
            print("Encerrando laboratório. Bom estudo para a prova!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
