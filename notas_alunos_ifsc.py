print("-----------------------------------------------")
print("IFSC")
print("-----------------------------------------------")
c = 1
maior_nota = 0
alunos = int(input("Quantos alunos tem na turma? "))
while c <= alunos:
    print("-----------------------------------------------")
    print(f"Aluno {c}")
    print("-----------------------------------------------")
    aluno = input("Nome do aluno: ")
    nota = int(input("Nota do aluno: "))
    if maior_nota < nota:
        maior_nota = nota
        nome_maior_nota = aluno
    c += 1
print("-----------------------------------------------")
print(f"O aluno com a maior nota foi {nome_maior_nota}, que tirou {maior_nota}.")
