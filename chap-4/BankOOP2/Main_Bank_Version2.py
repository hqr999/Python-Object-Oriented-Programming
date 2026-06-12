#Testando um programa usando contas 
#Versão 2, usando uma lista de contas 

#Traz todo o código do programa Account.py e sua classe Conta 

from Account import Conta

#Começa com uma lista vazia 
listaContas = [] 

#Criando duas contas 
oAccount = Conta('Joe', 100, 'SenhaJoe')
listaContas.append(oAccount)
print('A conta do Joe tem o número 0')


oAccount = Conta('Mary', 12345, 'MarySenha')
listaContas.append(oAccount)
print('A conta da Mary tem o número 1')

listaContas[0].mostra_info()
listaContas[1].mostra_info()
print() 


print('Chamando métodos das duas contas...')
listaContas[0].deposito(50, 'SenhaJoe')
listaContas[1].sacar(345, 'MarySenha')
listaContas[1].deposito(100, 'MarySenha')


listaContas[0].mostra_info()
listaContas[1].mostra_info()

print()
usuarioNome = input('Qual o nome do novo usuario para a nova conta ? ') 
usuarioSaldo = input('Qual é o saldo inicial para essa conta ? ')
usuarioSaldo = int(usuarioSaldo)
usuarioSenha = input('Qual é a senha para usar essa conta ?')
oAccount = Conta(usuarioNome, usuarioSaldo, usuarioSenha) 
listaContas.append(oAccount)

print('Criada uma nova conta, o número da conta é o 2')
listaContas[2].mostra_info()

listaContas[2].deposito(100, usuarioSenha)
usuarioSaldo = listaContas[2].pegaSaldo(usuarioSenha)
print() 
print('Depois de depositar 100, o saldo do usuário é: ',usuarioSaldo)



listaContas[2].mostra_info()
