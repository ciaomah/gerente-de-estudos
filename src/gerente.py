from datetime import datetime
import os

ARQUIVO_DADOS = "sessoes.txt"

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("ERROR: Deve digitar um valor inteiro válido.")

def registrar_sessao():
    print("\n--- REGISTRAR NOVA VERSÃO ---")
#coleta dados usando funcao de validacao
    fase = ler_inteiro("Digite o numero da fase estudada: ")
    minutos = ler_inteiro("Digite o tempo de estudo (em minutos): ")
    nota = ler_inteiro("Dê uma nota de 1 a 5 para a sessão: ")
# validacao simples da nota
    while nota < 1 or nota > 5:
        print("ERROR: A nova deve ser de 1 à 5.")
        nota = ler_inteiro("Dê uma nota de 1 a 5 para a sessão: ")

    data_atual = datetime.now().strftime("%d-%m-%Y %H:%M")
#salva no arquivo separando por ';'
    with open(ARQUIVO_DADOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_atual};{fase};{minutos};{nota}\n")

    print("Sessão registrada com sucesso!")

def gerar_relatorio():
    print("\n--- RELATORIO DE ESTUDOS ---")
# verifica se o arquivo existe antes de abrir
    if not os.path.exists(ARQUIVO_DADOS):
        print("Nenhuma sessão registrada ainda.")
        return

    total_sessoes = 0
    total_minutos = 0
    soma_notas = 0
    contador_fases = {} #dicionario p contar a frequencia

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(";")
# converte os textos para numeros
            fase = int(partes[1])
            minutos = int(partes[2])
            nota = int(partes[3])
# acumula valores para estatisticas
            total_sessoes += 1
            total_minutos += minutos
            soma_notas += nota
# contar a fase no dicionario
            if fase in contador_fases:
                contador_fases[fase] += 1
            else:
                contador_fases[fase] = 1

    # se o arquivo existir mas estiver vazio...
    if total_sessoes == 0:
        print("O arquivo está vazio!")
        return

    media_notas = soma_notas / total_sessoes

    fase_mais_estudada = None
    maior_quantidade = -1

    for fase, quantidade in contador_fases.items():
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            fase_mais_estudada = fase

    print(f"- Total de sessões: {total_sessoes}")
    print(f"- Total de minutos dedicados: {total_minutos} min")
    print(f"- Média das notas: {media_notas: .2f}")
    print(f"- Fase mais estudada: Fase {fase_mais_estudada} (Estudada {maior_quantidade} vezes)")

def menu():
    while True:
        print("\n____________________________")
        print("-> GERENTE DE ESTUDOS (v1) <-")
        print("\n____________________________")
        print("[1] Registrar Sessão")
        print("[2] Exibir Relatório")
        print("[3] Sair")
        print("\n____________________________")

        opcao = input("Escolha uma opcão: ").strip()

        if opcao == "1":
            registrar_sessao()
        elif opcao == "2":
            gerar_relatorio()
        elif opcao == "3":
            print("\nSaindo... Bons estudos e até logo!")
            break
        else:
            print("Opcão inválida. Escolha 1, 2 ou 3")

if __name__ == "__main__":
    menu()
