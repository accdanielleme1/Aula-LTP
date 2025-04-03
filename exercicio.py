''' Exercicio com companhia da professora'''

#classe sendo criado
class ContaBancaria:
    def __init__(self,cpf: str, saldo:float=0.0): #construtor
        self.cpf = cpf
        self.saldo = saldo

    def getSaldo(self): #Pegando saldo
        return self.saldo
    
    def getCPF(self): #Pegando CPF
        return self.cpf
    

    ''' Exercicio, adicionar saque e deposito'''
    
    





'''--------.----------.-------.---------.--------.------.--------------'''
'''contas criadas'''

conta1 = ContaBancaria("123.456.267-60") #primeira conta bancaria, dada por variavel, e add cpf e saldo na conta;

''' mostrando cpf e saldos'''

print('cpf da conta: ', conta1.getCPF())
print('saldo da conta: ', conta1.getSaldo() + conta1.setSaldo())

