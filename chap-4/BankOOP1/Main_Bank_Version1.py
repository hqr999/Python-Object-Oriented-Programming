#Programa de Teste 1 
#Versão 1, usando explicitamente variáveis para cada conta de banco (separadas)


from Account import Conta


oJoeConta = Conta('Joe', 100, 'UmaSenha')
print('Conta criada para ',oJoeConta.nome)




oMaryConta = Conta('Mary', 12345, 'SenhaDaMary')
print('Conta criada para ',oMaryConta.nome)


oJoeConta.mostra_info() 
oMaryConta.mostra_info()
print()


#Chama os métodos em contas diferentes 
print('Chamando os métodos das duas contas...')

oJoeConta.deposito(50, 'UmaSenha')
oMaryConta.sacar(621,'SenhaDaMary')
oMaryConta.deposito(709, 'SenhaDaMary')


oJoeConta.mostra_info()
oMaryConta.mostra_info()

print()
usuarioNome = input('Qual o nome do novo usuario para a nova conta ? ') 
usuarioSaldo = input('Qual é o saldo inicial para essa conta ? ')
usuarioSaldo = int(usuarioSaldo)
usuarioSenha = input('Qual é a senha para usar essa conta ?')
novaConta = Conta(usuarioNome, usuarioSaldo, usuarioSenha) 
novaConta.mostra_info()
novaConta.deposito(100,usuarioSenha) 
usersBalance = novaConta.pegaSaldo(usuarioSenha)
print()
print('Depois de depositar 100, o saldo do usuário é:',)
novaConta.mostra_info()
