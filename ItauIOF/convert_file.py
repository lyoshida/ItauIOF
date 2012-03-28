import codecs
import os

filename = os.path.abspath('PS_ST_S005_01_20120208.txt')

newfile = open('new.csv', mode='w')
newfile.write('Tipo de Registro,Data do movimento,Entidade,Cod. do Membro de Compensacao,Cod. do Participante,Cod. do Cliente,Tipo de Pessoa,No do Documento do Cliente,Vendas,Compras,Exposicao cambial liquida D-1,Variacao Exposicao d-1>d+0,Prov/Def\n')              

for line in codecs.open(filename):
    
    fields = line[0:2] + ','
    fields = fields + line[2:10] + ','
    fields = fields + line[10:13] + ','
    fields = fields + line[13:21] + ','
    fields = fields + line[21:29] + ','
    fields = fields + line[29:37] + ','
    fields = fields + line[37:38] + ','
    fields = fields + line[38:57] + ','
    fields = fields + line[57:69] + ','
    fields = fields + line[71:83] + ','
    fields = fields + line[85:98] + ','
    fields = fields + line[100:113] + ','
    fields = fields + line[115:116]

    newfile.write(fields + "\n")
newfile.close()
