# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo e Alexandre Leitão
# data: 30 de Setembro de 2013
# trabalho de Linguagens de Programação

import xlrd
from xlrd import open_workbook
import sqlite3
import script_distrito as sd

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
        self.conexao.text_factory = str
        self.c.execute('drop table if exists resultados_cna')
        #query para criação da tabela na base de dados
        self.c.execute('''create table if not exists resultados_cna
                        (cInstituicao int, cCurso int,
                        instituicao text, curso text, grau text,
                        vagasIniciais int, colocados int,
                        notaMaisBaixa double, vagasSobrantes int)''')
    

    #leitura de dados de um ficheiro excel
    def ler_ficheiro_excel(self, ficheiro):
        #guarda o ficheiro de excel na variável wb
        self.wb = open_workbook(ficheiro)
        #guarda a folha pretendida na variavel folha
        self.folha = self.wb.sheet_by_index(0)
        pass

    def passagem_de_dados(self, ficheiro_excel, ficheiro_base_de_dados):
        self.ler_ficheiro_excel(ficheiro_excel)
        self.criar_base_de_dados(ficheiro_base_de_dados)
        
        #Selecção da informação e introducção da mesma na base de dados
        for i in range(3, self.folha.nrows - 2):
            #query que envia uma linha excel para a base de dados
            self.c.execute("insert into resultados_cna values(?,?,?,?,?,?,?,?,?)",
                           (self.folha.cell(i,0).value,
                            self.folha.cell(i,1).value,
                            self.folha.cell(i,2).value,
                            self.folha.cell(i,3).value,
                            self.folha.cell(i,4).value,
                            self.folha.cell(i,5).value,
                            self.folha.cell(i,6).value,
                            self.folha.cell(i,7).value,
                            self.folha.cell(i,8).value))
            pass
        #Executa na base de dados os queries do cursor
        self.conexao.commit()
        pass
    def estatistica1(self, ficheiro_base_de_dados):
        r = ""
        data = []
        counter = 0
        self.c.execute("""select * from resultados_cna""")
        sd.tabela_escolas(self.c.fetchall())
        return data
    def estatistica2(self, ficheiro_base_de_dados):
        data = []
        self.c.execute('''select * from escolas''')
        sd.tabela_distritos(self.c.fetchall())
        pass
    def criacaoGraficoEntradasNorte(self, ficheiro_base_de_dados):
        self.c.execute('''select * from distritos''')        
        sd.graficoDEN(self, self.c.fetchall())
        pass
    def criacaoGraficoEntradasCentro(self, ficheiro_base_de_dados):
        self.c.execute('''select * from distritos''')        
        sd.graficoDEC(self, self.c.fetchall())
        pass
    def criacaoGraficoEntradasSul(self, ficheiro_base_de_dados):
        self.c.execute('''select * from distritos''')        
        sd.graficoDES(self, self.c.fetchall())
        pass
    def criacaoGraficoVagasNorte(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')        
		sd.graficoDVN(self, self.c.fetchall())
		pass
    def criacaoGraficoVagasCentro(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')        
		sd.graficoDVC(self, self.c.fetchall())
		pass
    def criacaoGraficoVagasSul(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')
		sd.graficoDVS(self, self.c.fetchall())
		pass
    def criacaoGraficoPermilagemNorte(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')
		sd.graficoDPN(self, self.c.fetchall())
		pass
    def criacaoGraficoPermilagemCentro(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')
		sd.graficoDPC(self, self.c.fetchall())
		pass
    def criacaoGraficoPermilagemSul(self,ficheiro_base_de_dados):
		self.c.execute('''select * from distritos''')
		sd.graficoDPS(self, self.c.fetchall())
		pass
    def criacaoGraficoEntradasEscolas(self,ficheiro_base_de_dados):
		self.c.execute('''select*from escolas''')
		sd.graficoEscolasEntradas(self, self.c.fetchall())
		pass
#tr = Trabalho()
#tr.passagem_de_dados('cna131fresultados.xls', 'trabalho')
#tr.estatistica1('trabalho')
#tr.estatistica2('trabalho')
#tr.criacaoGraficoEntradasEscolas('trabalho')
