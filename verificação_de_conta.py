print('=' * 25)
login = input("Já tem conta? S/N ")

if login == "N":
    nome_c = input("Digite o seu nome de usuario: ")
    senha_c = input("Digite sua senha: ")
    print("Parabéns! agora você pode fazer login.")
else:
    print("Faça login. ")

print('=' * 25)
print("Login: ")
print('=' * 25)

nome = input("Digite seu nome de usuario: ")
senha = input("Digite sua senha: ")
print('=' * 25)

if nome == nome_c and senha == senha_c:
    print("Acesso liberado!")
else:
    print("Acesso negado. Tente novamente.")