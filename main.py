# 1) Crie um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

grade = int(input("Insira sua nota acadêmica: "))

if grade >= 6:
    print("Parabéns, você foi aprovado!")
else:
    print("Você foi reprovado...")


# 2) Crie um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

age = int(input("Informe sua idade: "))

if age >= 16:
    print("Você está apto(a) a votar!")
else:
    print("Você não está apto(a) a votar.")


# 3) Crie um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

- A (90-100) – "Parabéns, você tirou A!"
- B (80-89) – "Muito bem, você tirou B."
- C (70-79) – "Bom trabalho, você tirou C."
- D (60-69) – "Fique atento, você tirou D."
- F (menos de 60) – "Estude um pouco mais, você tirou F."

grade = int(input("Informe sua nota: "))

if grade >= 90 and grade <=100:
    print("Parabéns! sua classificação foi A!")
elif grade >= 80 and grade <=89:
    print("Muito bem, sua classificação foi B.")
elif grade >=70 and grade <=79:
    print("Sua classificação foi C.")
elif grade >= 60 and grade <=69:
    print("Sua classificação foi D.")
elif grade <60 and grade >=1:
    print("Fique atento, sua classificação foi F.")
else:
    print("Valor inválido, tente novamente.")


# 4) Crie um programa que peça dois números ao usuário e exiba a soma deles.

numberX = int(input("Digite um número: "))
numberY = int(input("Digite o segundo número: "))

print(f"\nA soma dos números '{numberX}' e '{numberY}' é {numberX + numberY}.")


# 5) Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

password = "Python123"
typed_pass = input("Digite sua senha: ")

print("Senha correta" if typed_pass in password else "Senha incorreta")


# 6) Exiba os números de 1 a 10 usando um loop while. 
#  
num = 1

while num <= 10:
    print(num)
    num+=1


# 7) Você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente.

numbers = [8, 3, 10, 1, 5]
numbers.sort()

print(numbers)


# 8) Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.

names = ('Ana', 'Bruno', 'Carla', 'Daniel')
print(f"{names[0]} - {names[-1]}" )


# 9) Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.

def double_number(num):
    return num * 2

number_input = int(input("Digite um número: "))
print(f"O dobro de {number_input} é {double_number(number_input)}.")


# 10) O sistema precisa contar quantas letras há em um nome:

def name_word (name):
    return print(f"O nome '{name}' possui {len(name.replace(" ", ""))} letras.")

name_input = input("Digite um nome: ")
name_word(name_input)

