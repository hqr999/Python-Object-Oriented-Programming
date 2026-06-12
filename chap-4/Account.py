class Conta():
    def __init__(self,nome,saldo,senha):
        self.nome = nome 
        self.saldo = saldo 
        self.senha = senha 

    def deposito(self,qtd_deposito,senha):
        if senha != self.senha:
            print('Desculpe, senha incorreta')
            return None 
        if qtd_deposito < 0:
            print('Você não pode depositar um valor negativo')
            return None 

        self.saldo += qtd_deposito
        return self.saldo

    def sacar(self,qtd_saque,senha):
        if senha != self.senha:
            print('Desculpe, senha incorreta')
            return None 
        if qtd_saque > self.saldo:
            print('Você não pode depositar um valor negativo')
            return None 

        self.saldo -= qtd_saque
        return self.saldo

    def pegaSaldo(self,senha):
        if self.senha != senha:
            print('Desculpe, senha incorreta')
            return None 

        return self.saldo

    def mostra_info(self):
        print('         Nome:',self.nome)
        print('         Saldo:',self.saldo)
        print('         Senha:',self.senha)
        print()


