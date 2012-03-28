# coding: utf-8

# to-do list: -usar codecs.open() em vez do file.open()
# sugestão: poderia usar o with statement [file] as file, se acontecer uma excecao ele fecha sem precisar usar file.close()

import os
import codecs
import sqlite3

ItauDB = sqlite3.connect('Itau.db')
querycursor = ItauDB.cursor()

def CreateTable():
    querycursor.execute('''CREATE TABLE A010 
                        (id INT PRIMARY KEY, tiporeg TEXT, DataMov TEXT, Entidade TEXT,
                        CodMemComp TEXT, CodPart TEXT, TipoPessoa TEXT, NumDocCliente TEXT,
                        Mercado TEXT, Mercadoria TEXT, Serie TEXT, TipoOpc TEXT,
                        NatQA TEXT, QtdadeQA TEXT, NatQ TEXT, QtdadeQ TEXT, ValorRef TEXT,
                        ValorTxBase TEXT, ValorDelta TEXT, ValorTxJurMoeda TEXT,
                        ValorCC TEXT, ValorVol TEXT, ValorAtObj TEXT, ValorPrEx TEXT)2
                        ''')

class Itauiof(object):
    
    def __init__(self):
        self.current_path = os.getcwd() #guarda caminho atual
    
    def convertA010(self):
        for file in self.get_files()[1]:
            
            txtfile = self.current_path + '/' + file
            print file[:-3]+'csv'
            csvfile = open(file[:-3]+'csv', mode='w')
            csvfile.write('Tipo de Registro,Data do Movimento,Entidade,Cod do Membro de compensacao,Cod do Participante,Cod do Cliente,Tipo de Pessoa,Num do Documento do Cliente,Mercado,Mercadoria,Serie,Tipo Opcao,Natureza - QA,Quantidade - QA,Natureza - QA,Quantidade - QA,Valor de Referencia,Valor Taxa Base,Valor Delta,Valor Taxa de Juros Moeda Utilizada-Pre (%a.a.),Valor do Cupom Cambial (%a.a.),Valor da Volatilidade (%a.a.),Valor do Ativo-Objeto,Valor do Preco do Exercicio Opcao, Provisorio/Definitivo\n')             
            
            for line in codecs.open(txtfile):
                
                fields = line[0:2] + ',' #Tipo de Registro
                fields = fields + line[2:10] + ',' #Data Movimento
                fields = fields + line[10:13] + ',' #Entidade
                fields = fields + line[13:21] + ',' #Cod Membro Comp
                fields = fields + line[21:29] + ',' #Cod Participante
                fields = fields + line[29:37] + ',' #Cod Cliente
                fields = fields + line[37:38] + ',' # Tipo de Pessoa
                fields = fields + line[38:57] + ',' #Num do doc do cliente
                fields = fields + line[57:60] + ',' #Mercado
                fields = fields + line[60:63] + ',' #Mercadoria
                fields = fields + line[63:67] + ',' #Serie
                fields = fields + line[67:68] + ',' #Tipo Opcao
                fields = fields + line[68:69] + ',' #Natureza - QA
                fields = fields + str(int(line[69:86])/100) + ',' #Qtdade - QA
                fields = fields + line[86:87] + ',' #Natureza - Q
                fields = fields + str(int(line[87:104])/100) + ',' #Qtdade - Q
                fields = fields + str(int(line[104:121])/100) + ',' #Valor Ref
                fields = fields + str(int(line[121:140])/10000) + ',' #Valor Tx Base
                fields = fields + str(int(line[140:158])/1000) + ',' #Valor Delta
                fields = fields + str(int(line[158:177])/10000) + ',' #Valor Tx Juros Moeda
                fields = fields + str(int(line[177:196])/10000) + ',' #Valor Cupom Cambial
                fields = fields + str(int(line[196:215])/10000) + ',' #Valor Vol
                fields = fields + str(int(line[215:233])/1000) + ',' #Valor Ativo-ojb
                fields = fields + str(int(line[233:251])/1000) + ',' #Valor Preco Ex
                fields = fields + line[251:252] #Prov/Def
                
                csvfile.write(fields + "\n")
            csvfile.close()
    
    def convertS005(self):
        
        for file in self.get_files()[0]:
            
            txtfile = self.current_path + '/' +file
            print file[:-3]+'csv'
            csvfile = open(file[:-3]+'csv', mode='w')
            csvfile.write('Tipo de Registro,Data do movimento,Entidade,Cod. do Membro de Compensacao,Cod. do Participante,Cod. do Cliente,Tipo de Pessoa,No do Documento do Cliente,Vendas,Compras,Exposicao cambial liquida D-1,Variacao Exposicao d-1>d+0,Provisorio/Definitivo\n')              
            
            for line in codecs.open(txtfile):
                
                fields = line[0:2] + ',' #Tipo de reg
                fields = fields + line[2:10] + ',' #Data do Mov
                fields = fields + line[10:13] + ',' #Entidade
                fields = fields + line[13:21] + ',' #Cod Membro de Comp
                fields = fields + line[21:29] + ',' #Cod do Participante
                fields = fields + line[29:37] + ',' #Cod Cliente
                fields = fields + line[37:38] + ',' #Tipo de pessoa
                fields = fields + line[38:57] + ',' #Num do documento do cliente
                fields = fields + str(int(line[57:71])/100) + ',' #Vendas
                fields = fields + str(int(line[71:85])/100) + ',' #Compras
                fields = fields + str(int(line[85:100])/100) + ',' #Exposicao cambial liquida
                fields = fields + str(int(line[100:115])/100) + ',' #Variacao Exposicao
                fields = fields + line[115:116] #Prov/Def
            
                csvfile.write(fields + "\n")
            csvfile.close()
        
    def get_files(self):
        """ Returns 2 list of strings containing files names of current directory"""
        filesS005 = []
        filesA010 = []
        for file in os.listdir(self.current_path):
            if file[-3:] == 'txt':
                if file[:10] == 'PS_ST_S005':
                    filesS005.append(file)
                if file[:10] == 'PS_ST_A010':
                    filesA010.append(file)
        return filesS005,filesA010
        
