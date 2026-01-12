alunos = []

def situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def calcular_media(notas):
    return sum(notas) / len(notas)

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Ver alunos")
    print("0 - Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")

        notas = []
        for i in range(1, 4):
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)

        media = calcular_media(notas)

        aluno = {
            "nome": nome,
            "media": media,
            "situacao": situacao(media)
        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(
                    "Aluno:", aluno["nome"],
                    "| Média:", aluno["media"],
                    "| Situação:", aluno["situacao"]
                )

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Digite uma opção válida.")

print("Obrigado por usar o programa!")
