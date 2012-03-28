# coding: utf-8

# to-do list: -usar codecs.open() em vez do file.open()
# sugestão: poderia usar o with statement [file] as file, se acontecer uma excecao ele fecha sem precisar usar file.close()

import os
import codecs #@UnresolvedImport
import sqlite3 #@UnresolvedImport
import glob #biblioteca para ler arquivos @UnresolvedImport

ItauDB = sqlite3.connect('Itau.db')
querycursor = ItauDB.cursor()

S005_TITLES = ['Tipo de Registro,Data do movimento,Entidade,Cod. do Membro de Compensacao,Cod. do Participante,Cod. do Cliente,Tipo de Pessoa,No do Documento do Cliente,Vendas,Compras,Exposicao cambial liquida D-1,Variacao Exposicao d-1>d+0,Provisorio/Definitivo']
A010_TITLES = ['Tipo de Registro,Data do Movimento,Entidade,Cod. do Membro de compensacao,Cod. do Participante,Cod. do Cliente,Tipo de Pessoa,No do Documento do Cliente,Mercado,Mercadoria,Serie,Tipo Opcao,Natureza - QA,Quantidade - QA,Natureza - QA,Quantidade - QA,Valor de Referencia,Valor Taxa Base,Valor Delta,Valor Taxa de Juros Moeda Utilizada-Pre (%a.a.),Valor do Cupom Cambial (%a.a.),Valor da Volatilidade (%a.a.),Valor do Ativo-Objeto,Valor do Preco do Exercicio Opcao, Provisorio/Definitivo']

def CreateTableA010():
    try:
        querycursor.execute('''CREATE TABLE A010 
                            (id INT PRIMARY KEY, tiporeg TEXT, DataMov TEXT, Entidade TEXT,
                            CodMemComp TEXT, CodPart TEXT, TipoPessoa TEXT, NumDocCliente TEXT,
                            Mercado TEXT, Mercadoria TEXT, Serie TEXT, TipoOpc TEXT,
                            NatQA TEXT, QtdadeQA TEXT, NatQ TEXT, QtdadeQ TEXT, ValorRef TEXT,
                            ValorTxBase TEXT, ValorDelta TEXT, ValorTxJurMoeda TEXT,
                            ValorCC TEXT, ValorVol TEXT, ValorAtObj TEXT, ValorPrEx TEXT)
                            ''')
    except sqlite3.OperationalError:
        print 'Database already exists. Nothing done.'
    
def CreateTableS005():
    try:
        querycursor.execute('''CREATE TABLE S005 
                            (id INT PRIMARY KEY, tiporeg TEXT, DataMov TEXT, Entidade TEXT,
                            CodMemComp TEXT, CodPart TEXT, CodCliente TEXT, TipoPessoa TEXT,
                            NumDocCliente TEXT, Vendas TEXT, Compras TEXT, ExpCambLiq TEXT,
                            VarLiq TEXT, ProvDef TEXT)
                            ''')
    except sqlite3.OperationalError:
        print 'Database already exists. Nothing done.'

def DelTableA010():
    if raw_input('This will delete Table A010. Continue? (yes/no):') == 'yes':
        try:
            querycursor.execute(''' DROP TABLE A010 ''')
            print 'Table A010 deleted.'
        except sqlite3.OperationalError:
            print 'Table A010 not found'
    else:
        print 'Cancelled. No changes.'
    
def DelTableS005():
    if raw_input('This will delete Table S005. Continue? (yes/no):') == 'yes':
        try:
            querycursor.execute(''' DROP TABLE S005 ''')
            print 'Table S005 deleted.'
        except sqlite3.OperationalError:
            print 'Table S005 not found'
    else:
        print 'Cancelled. No changes.'

def ShowA010():
    #implementar
    pass    
    
def ShowS005():
    #implementar
    a = querycursor.execute(''' SELECT * FROM S005 ''')
    
class Itauiof(object):
    
    def __init__(self):
        self.current_path = os.getcwd() #guarda caminho atual
    
    def convertA010_CSV(self):
        
        for file in self.get_A010files():
            
            print 'creating ' +  file[:-3]+'csv'
            csvfile = open(file[:-3]+'csv', mode='w')          
            csvfile.write(','.join(A010_TITLES) + '\n')
            for line in codecs.open(file):
                csvfile.write(','.join(self.lineA010(line)) + "\n")
            csvfile.close()
    
    def convertS005_CSV(self):
        
        for file in self.get_S005files():
            
            print 'creating ' +  file[:-3]+'csv'
            csvfile = open(file[:-3]+'csv', mode='w')
            csvfile.write(','.join(S005_TITLES) + '\n')
            for line in codecs.open(file):
                csvfile.write(','.join(self.lineS005(line)) + "\n")
            csvfile.close()
        
    def saveS005(self):
        for file in self.get_S005files():
            with file as source:
                pass
        
    def get_S005files(self):
        """ Returns a list of strings containing full path of S005 files inside the current directory """
        filesS005 = []
        filesS005 = glob.glob(self.current_path + '/PS_ST_S005*.txt')
        return filesS005
    
    def get_A010files(self):
        """ Returns a list of strings containing full path of A010 files inside the current directory """
        filesA010 = []
        filesA010 = glob.glob(self.current_path + '/PS_ST_A010*.txt')
        return filesA010
        
    def lineS005(self,line):
        ''' Returns a list with contents of a S005 line (strings) '''
        contents = []
        contents.append(line[0:2]) #Tipo de reg
        contents.append(line[2:10]) #Data do Mov
        contents.append(line[10:13]) #Entidade
        contents.append(line[13:21]) #Cod Membro de Comp
        contents.append(line[21:29]) #Cod do Participante
        contents.append(line[29:37]) #Cod Cliente
        contents.append(line[37:38]) #Tipo de Pessoa
        contents.append(line[38:57]) #Num do documento do cliente
        contents.append(str(int(line[57:71])/100)) #Vendas
        contents.append(str(int(line[71:85])/100)) #Compras
        contents.append(str(int(line[85:100])/100)) #Exposicao cambial liquida
        contents.append(str(int(line[100:115])/100)) #Variacao Exposicao
        contents.append(line[115:116]) #Prov/Def
        return contents
    
    def lineA010(self,line):
        ''' Returns a list with contents of a A010 line (strings) '''
        contents = []
        contents.append(line[0:2]) #Tipo de Registro
        contents.append(line[2:10]) #Data Movimento
        contents.append(line[10:13]) #Entidade
        contents.append(line[13:21]) #Cod Membro Comp
        contents.append(line[21:29]) #Cod Participante
        contents.append(line[29:37]) #Cod Cliente
        contents.append(line[37:38]) # Tipo de Pessoa
        contents.append(line[38:57]) #Num do doc do cliente
        contents.append(line[57:60]) #Mercado
        contents.append(line[60:63]) #Mercadoria
        contents.append(line[63:67]) #Serie
        contents.append(line[67:68]) #Tipo Opcao
        contents.append(line[68:69]) #Natureza - QA
        contents.append(str(int(line[69:86])/100)) #Qtdade - QA
        contents.append(line[86:87]) #Natureza - Q
        contents.append(str(int(line[87:104])/100)) #Qtdade - Q
        contents.append(str(int(line[104:121])/100)) #Valor Ref
        contents.append(str(int(line[121:140])/10000)) #Valor Tx Base
        contents.append(str(int(line[140:158])/1000)) #Valor Delta
        contents.append(str(int(line[158:177])/10000)) #Valor Tx Juros Moeda
        contents.append(str(int(line[177:196])/10000)) #Valor Cupom Cambial
        contents.append(str(int(line[196:215])/10000)) #Valor Vol
        contents.append(str(int(line[215:233])/1000)) #Valor Ativo-ojb
        contents.append(str(int(line[233:251])/1000)) #Valor Preco Ex
        contents.append(line[251:252]) #Prov/Def
        return contents
        
    def savedbS005(self,file):

        ''' Saves a S005 file to Database '''
    