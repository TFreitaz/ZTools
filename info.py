import pickle


class CPF(str):
    def __init__(self, cpf):
        cpf = str(cpf)
        self.full = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}'
        
    def info(self):
        print('CPF:', self.full)
        
class Phone(str):
    def __init__(self, number):
        self.isCell = False
        self.isResidential = False
        self.operator = None
        
    def set_data(self, cell = False, residential = False, operator = None):
        if cell: self.isCell = cell
        if residential: self.isResidential = residential
        if operator: self.operator = operator
            
    def info(self):
        print('Número:', str(self))
        if self.isCell: print('Tipo: Celular')
        if self.isResidential: print('Tipo: Residencial')
        if self.operator: print('Operadora:', self.operator)
            
class RG(str):
    def __init__(self, rg):
        rg = str(rg)
        self.full = f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[-1]}'
        self.SSP = None
        self.exp_date = None
        
    def set_data(self, SSP = None, exp_date = None):
        if SSP: self.SSP = SSP
        if exp_date: self.exp_date = exp_date
            
    def info(self):
        print('RG:', self.full)
        if self.SSP: print('SSP:', self.SSP)
        if self.exp_date: print('Data de Expiração:', self, exp_date)
    
class CNH(str):
    def __init__(self, cnh):
        self.val = None
        self.first = None
        self.cat = None
        self.emiss_date = None
        self.local = None
        
    def set_data(self, val = None, first = None, cat = None, emiss_date = None, local = None):
        if val: self.val = val
        if first: self.first = first
        if cat: self.category = cat
        if emiss_date: self.emiss_date = emiss_date
        if local: self.local = local
            
    def info(self):
        print('CNH:', str(self))
        if self.val: print('Validade:', self.val)
        if self.first: print('Primeira Habilitação:', self.first)
        if self.cat: print('Categoria:', self.category)
        if self.emiss_date: print('Data de Emissão:', self.emiss_date)
        if self.local: print('Local', self.local)
            
class BankCard():
    def __init__(self, cardnum = None, bank = None, ingress = None, val = None, CVS = None, psword = None, psword2 = None):
        self.number = str(cardnum)
        self.bank = bank
        self.ingress = ingress
        self.val = val
        self.CVS = CVS
        self.psword = psword
        self.psword2 = psword2
            
    def set_data(self, cardnum = None, bank = None, ingress = None, val = None, CVS = None, psword = None, psword2 = None):
        if cardnum: self.number = str(cardnum)
        if bank: self.bank = bank
        if ingress: self.ingress = ingress
        if val: self.val = val
        if CVS: self.CVS = CVS
        if psword: self.psword = psword
        if psword2: self.psword = psword2
            
    def info(self):
        if self.bank: print('Banco:', self.bank)
        if self.number: print('Número:', self.number)
        if self.ingress: print('Emissão:', self.ingress)
        if self.val: print('Validade:', self.val)
        if self.CVS: print('CVS:', self.CVS)
        if self.psword: print('Senha:', self.psword)
        if self.psword2: print('Senha 2:', self.psword2)

class Pessoa():
    def __init__(self, name):
        self.name = name
        self.nicknames = []
        self.bankcards = {}
        self.RG = None
        self.CNH = None
        self.CPF = None
        self.phones = []
        self.accessPswords = []
        self.pswords = []
        
    def insertAcessPassword(self, psword):
        self.accessPswords.append(str(psword))
        
    def insertRG(self, *args, **kwargs):
        self.RG = RG(*args, **kwargs)
    
    def insertCPF(self, *args, **kwargs):
        self.CPF = CPF(*args, **kwargs)
        
    def insertCNH(self, *args, **kwargs):
        self.CNH = CNH(*args, **kwargs)
        
    def insertBankCard(self, *args, **kwargs):
        card = BankCard(*args, **kwargs)
        name = ''
        if card.bank:
            name += card.bank
        name += card.number[-4:]
        self.bankcards[name] = card
    
    def insertPhone(self, *args, **kwargs):
        self.phones.append(Phone(*args, **kwargs))
        
    def insertPassword(self, psword):
        self.pswords.append(psword)
        
    def info(self, hide_bankcards = True):
        print('Nome:', self.name)
        if len(self.nicknames) > 0: print('Apelidos:', ', '.join(self.nicknames) + '.')
        if self.RG: self.RG.info()
        if self.CPF: self.CPF.info()
        if self.CNH: self.CNH.info()
        for phone in self.phones:
            phone.info()
        if not hide_bankcards:
            for card in self.bankcards.keys():
                self.bankcards[card].info()
                
class Pessoas():
    def __init__(self):
        self.pessoas = {}
        
    def insertPerson(self, *args, **kwargs):
        pessoa = Pessoa(*args, **kwargs)
        self.pessoas[pessoa.name] = pessoa
        
    def listPeople(self):
        for pessoa in self.pessoas.keys():
            print(pessoa)
            
    def getPerson(self, name):
        pessoa = self.pessoas[name]
        access = len(pessoa.accessPswords) == 0
        if not access:
            if input() in pessoa.accessPswords:
                access = True
        if access:
            return pessoa
        
    def getPeople(self):
        people = []
        psword = input()
        for _pessoa in self.pessoas.keys():
            pessoa = self.pessoas[_pessoa]
            access = len(pessoa.accessPswords) == 0
            if not access:
                if psword in pessoa.accessPswords:
                    access = True
            if access:
                people.append(pessoa)
        return people
                
    def SavePeople(self):
        with open('C:/Users/thale/Anaconda3/Lib/site-packages/ztools/people.pkl', 'wb') as p:
            pickle.dump(self, p, pickle.HIGHEST_PROTOCOL)
            
def LoadPeople():
    with open('C:/Users/thale/Anaconda3/Lib/site-packages/ztools/people.pkl', 'rb') as p:
        return pickle.load(p)
    