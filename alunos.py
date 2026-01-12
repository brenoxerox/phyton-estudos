opcao = 1

alunos = []
medias = []
situacoes = []

def situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


while opcao != 0:
    print("\n1 - Cadastrar aluno")
    print("2 - Ver alunos")
    print("0 - Sair")

    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)

        notas_temporarias = []

        for i in range(1, 4):
            nota = float(input(f"Digite a nota {i}: "))
            notas_temporarias.append(nota)

        media = calcular_media(
            notas_temporarias[0],
            notas_temporarias[1],
            notas_temporarias[2]
        )

        medias.append(media)
        situacoes.append(situacao(media))

        print("Aluno cadastrado com sucesso!")

    elif opcao == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            ordem = 0
            while ordem < len(alunos):
                print(
                    "Aluno:", alunos[ordem],
                    "| Média:", medias[ordem],
                    "| Situação:", situacoes[ordem]
                )
                ordem += 1

    elif opcao == 0:
        print("Encerrando o programa...")

    else:
        print("Digite uma opção válida.")

print("Obrigado por usar o programa!")
