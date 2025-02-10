import os


def switch_case():
    cont = 1
    while cont != 0:
        print(
            "\nDigite um número de 1-10, correspondente ao exercício que queira executar\nou digite '0' para sair: ")
        print("\n 1: Restaurando as Regras Escolares \n 2: O Sistema Eleitoral Secreto \n 3: Recuperando o Sistema de Notas \n 4: Restaurando a Identificação de Números \n 5: Recuperando o Cofre de Segurança \n 6: Reforçando a Segurança e a Contagem do Sistema \n 7: Organizando a Lista \n 8: Acessando os Registros de Alunos \n 9: Calculando Dobro de um Número \n 10: Contando Letras \n 0: Sair")

        cont = int(input("\nEscolha uma opção: "))

        match cont:
            case 1:
                os.system('cls')
                # 1) Crie um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).
                print("\n1) Restaurando as Regras Escolares\n")
                grade = int(input("Insira sua nota acadêmica: "))
                if grade >= 6:
                    print("Parabéns, você foi aprovado!")
                else:
                    print("Você foi reprovado...")

            case 2:
                os.system('cls')
                # 2) Crie um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).
                print("\n2) O Sistema Eleitoral Secreto\n")
                age = int(input("Informe sua idade: "))
                if age >= 16:
                    print("Você está apto(a) a votar!")
                else:
                    print("Você não está apto(a) a votar.")

            case 3:
                os.system('cls')
                # 3) Crie um programa que peça a nota do aluno e imprima sua classificação conforme a escala
                print("\n3) Recuperando o Sistema de Notas\n")
                grade = int(input("Informe sua nota: "))
                if grade >= 90 and grade <= 100:
                    print("Parabéns! sua classificação foi A!")
                elif grade >= 80 and grade <= 89:
                    print("Muito bem, sua classificação foi B.")
                elif grade >= 70 and grade <= 79:
                    print("Sua classificação foi C.")
                elif grade >= 60 and grade <= 69:
                    print("Sua classificação foi D.")
                elif grade < 60 and grade >= 1:
                    print("Fique atento, sua classificação foi F.")
                else:
                    print("Valor inválido, tente novamente.")

            case 4:
                os.system('cls')
                # 4) Crie um programa que peça dois números ao usuário e exiba a soma deles.
                print("\n4) Restaurando a Identificação de Números\n")
                numberX = int(input("Digite um número: "))
                numberY = int(input("Digite o segundo número: "))
                print(
                    f"\nA soma dos números '{numberX}' e '{numberY}' é {numberX + numberY}.")

            case 5:
                os.system('cls')
                # 5) Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".
                print("\n5) Recuperando o Cofre de Segurança\n")
                password = "Python123"
                typed_pass = input("Digite sua senha: ")
                print("Senha correta" if typed_pass in password else "Senha incorreta")

            case 6:
                os.system('cls')
                # 6) Exiba os números de 1 a 10 usando um loop while.
                print("\n6) Reforçando a Segurança e a Contagem do Sistema \n")
                num = 1
                while num <= 10:
                    print(num)
                    num += 1

            case 7:
                os.system('cls')
                # 7) Você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente.
                print("\n7) Organizando a Lista\n")
                numbers = [8, 3, 10, 1, 5]
                numbers.sort()
                print(numbers)

            case 8:
                os.system('cls')
                # 8) Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.
                print("\n8) Acessando os Registros de Alunos\n")
                names = ('Ana', 'Bruno', 'Carla', 'Daniel')
                print(f"{names[0]} - {names[-1]}")

            case 9:
                os.system('cls')
                # 9) Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
                print("\n9) Calculando Dobro de um Número\n")

                def double_number(num):
                    return num * 2
                number_input = int(input("Digite um número: "))
                print(
                    f"O dobro de {number_input} é {double_number(number_input)}.")

            case 10:
                os.system('cls')
                # 10) O sistema precisa contar quantas letras há em um nome:
                print("\n10) Contando Letras \n")

                def name_word(name):
                    return print(f"O nome '{name}' possui {len(name.replace(" ", ""))} letras.")
                name_input = input("Digite um nome: ")
                name_word(name_input)

            case 0:
                os.system('cls')
                print("Saindo...")
                print("\nAté mais!")

            case _:
                os.system('cls')
                print("O termo digitado é inválido, escolha um número de 1 a 10.")


print("\n\n____________________________________________________________________________")
print(
    "-------------------------Desafio 01-----------------------------------------")
switch_case()
