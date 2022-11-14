#classe
class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = 0 #ou None

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'. format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor


#programa
conta_Lira = ContaCorrente("Lira", "111.222.333-45")
#print(conta_Lira.cpf)
conta_Lira.consultar_saldo()

#depositando um dinheirinho na conta
conta_Lira.depositar(10000)
conta_Lira.consultar_saldo()

#sacando um dinheirinho na conta
conta_Lira.sacar_dinheiro(10500)

print('Saldo Final')
conta_Lira.consultar_saldo()




