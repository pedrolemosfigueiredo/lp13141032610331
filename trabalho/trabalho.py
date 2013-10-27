# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo
# data: 30 de Setembro de 2013
# trabalho de Linguagens de Programação

import xlrd
from xlrd import open_workbook
import sqlite3

class Trabalho:
    def __init__(self):
        
        pass
    def criar_base_de_dados(self, ficheiro):
        #criação da base de dados com o ficheiro de nome basededados.db e
        #guardá-la na variável conexao
        self.conexao = sqlite3.connect(ficheiro)
        #criação da instância cursor que permite mandar queries para a base
        #de dados
        self.c = self.conexao.cursor()
        #criação da tabela na base de dados
        self.c.execute('''create table if not exists resultados_cna
                        (cInstituicao integer, cCurso integer,
                        instituicao text, curso text, grau text,
                        vagasIniciais integer, colocados integer,
                        notaMaisBaixa double, vagasSobrantes integer)''')
    

    #leitura de dados de um ficheiro excel
    def ler_ficheiro_excel(self, ficheiro):
        #guarda o ficheiro de excel na variável wb
        self.wb = open_workbook(ficheiro)
        #guarda a folha pretendida na variavel folha
        self.folha = self.wb.sheet_by_index(0)
        print self.folha.nrows
        pass

    def passagem_de_dados(self, ficheiro_excel, ficheiro_base_de_dados):
        self.ler_ficheiro_excel(ficheiro_excel)
        self.criar_base_de_dados(ficheiro_base_de_dados)
        for i in range(3, self.folha.nrows):
            print self.folha.cell(i, 0).value
            print self.folha.cell(i,8).value
            self.c.execute('insert into resultados_cna values(?,?,?,?,?,?,?,?,?)',
                           (self.folha.cell(i,0).value,
                            self.folha.cell(i,1).value,
                            self.folha.cell(i,2).value,
                            self.folha.cell(i,3).value,
                            self.folha.cell(i,4).value,
                            self.folha.cell(i,5).value,
                            self.folha.cell(i,6).value,
                            self.folha.cell(i,7).value,
                            self.folha.cell(i,8).value,
                            self.folha.cell(i,9).value))
            print self.folha
            '''self.c.execute('alter table resultados_cna add column ?',
                           self.folha.cell(i,0).value)'''
            pass
        pass

    pass
Trabalho().passagem_de_dados('cna131fresultados.xls', 'trabalho')
