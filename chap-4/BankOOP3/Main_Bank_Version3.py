# Programa teste usando contas
# Versão 3, usando um dicionário de contas


# Traz todo o código do arquivo Account.py
from Account import *

contasDicionario = {}
proxContaNum = 0

oAcc = Conta("Joe", 100, "JoeSenha")
contaJoeNum = proxContaNum

contasDicionario[contaJoeNum] = oAcc
print("Número da conta do Joe é:", contaJoeNum)
proxContaNum += 1

oAcc = Conta("Mary", 12345, "MarySenha")
contaMaryNum = proxContaNum

contasDicionario[contaMaryNum] = oAcc
print("Número da conta da Mary é:", contaMaryNum)
proxContaNum += 1

contasDicionario[contaJoeNum].mostra_info()
contasDicionario[contaMaryNum].mostra_info()
print()


#Chamando os métodos em duas contas diferentes
print()
contasDicionario[contaJoeNum].deposito(50, 'SenhaJoe')
contasDicionario[contaMaryNum].sacar(345, 'MarySenha')
contasDicionario[contaMaryNum].deposito(100, 'MarySenha')

print()
usuarioNome = input('Qual o nome do novo usuario para a nova conta ? ') 
usuarioSaldo = input('Qual é o saldo inicial para essa conta ? ')
usuarioSaldo = int(usuarioSaldo)
usuarioSenha = input('Qual é a senha para usar essa conta ?')
oAcc = Conta(usuarioNome, usuarioSaldo, usuarioSenha) 
novaContaNum = proxContaNum
contasDicionario[novaContaNum] = oAcc

print('O número da conta da nova conta é: ',novaContaNum)
proxContaNum += 1

contasDicionario[novaContaNum].mostra_info()

contasDicionario[novaContaNum].deposito(100, usuarioSenha)
usuarioSaldo = contasDicionario[novaContaNum].pegaSaldo(usuarioSenha)
print() 
print('Depois de depositar 100, o saldo do usuário é:',usuarioSaldo)


contasDicionario[novaContaNum].mostra_info()

