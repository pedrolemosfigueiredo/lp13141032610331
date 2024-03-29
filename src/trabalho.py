# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo e Alexandre Leitão
# data: 30 de Setembro de 2013
# trabalho de Linguagens de Programação

import xlrd
from xlrd import open_workbook
import sqlite3
import script as sd
import csv

"""
Class which makes all the the CVS, DataBase and excell operations and the
nedded queries for graphics
"""

class Trabalho:
    
    def __init__(self):
        pass
    
    def criar_base_de_dados(self, ficheiro):
        """
            Creates the database
            @param ficheiro gives the name of the database
        """
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
        """
            Reads one given excell file and stores the desired sheet
            @param ficheiro the name of the excell file
        """
        #guarda o ficheiro de excel na variável wb
        self.wb = open_workbook(ficheiro)
        #guarda a folha pretendida na variavel folha
        self.folha = self.wb.sheet_by_index(0)
        pass

    def passagem_de_dados(self, ficheiro_excel, ficheiro_base_de_dados):
        """
            Passes the data from the excell file to the the database
            @param ficheiro_excel name of the excell file
            @param ficheiro_base_de_dados name of the database
        """
        self.ler_ficheiro_excel(ficheiro_excel)
        self.criar_base_de_dados(ficheiro_base_de_dados)
        pass
        
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
        """
            Creates the query which will give the data nedded for the creation of
            schools(escolas) table
            @param ficheiro_base_de_dados name of the database
            @return return the 
        """
        self.c.execute("""select * from resultados_cna""")
        sd.tabela_escolas(self.c.fetchall())
        pass

    def estatistica2(self, ficheiro_base_de_dados):
        """
            Creates the query which will give the data nedded for the creation of
            districts(distritos) table from the school table
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from escolas''')
        sd.tabela_distritos(self.c.fetchall())
        pass
    
    def estatisticasCSV(self, ficheiro_base_de_dados):
        """
            Creates the csv files which will hold the estatistics for schools 
            and districts 
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from escolas''')
        csvWriter = csv.writer(open('institutos.csv','wt'))
        csvWriter.writerows(self.c)
        del csvWriter
        self.c.execute('''select * from distritos''')
        csvWriter = csv.writer(open('distritos.csv','wt'))
        csvWriter.writerows(self.c)
        del csvWriter
        pass
    
    def criacaoGraficoEntradasNorte(self, ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in the north
            @param ficheiro_base_de_dados name of the database
        """
        if 'conexao' in globals():
            print 'exists'
            pass
        self.c.execute('''select * from distritos''')
        sd.graficoDEN(self, self.c.fetchall())
        pass
    
    def criacaoGraficoEntradasCentro(self, ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in the center
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')
        sd.graficoDEC(self, self.c.fetchall())
        pass
    
    def criacaoGraficoEntradasSul(self, ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in the south
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')        
        sd.graficoDES(self, self.c.fetchall())
        pass
    
    def criacaoGraficoVagasNorte(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in the north
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')        
        sd.graficoDVN(self, self.c.fetchall())
        pass
    
    def criacaoGraficoVagasCentro(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in the center
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')        
        sd.graficoDVC(self, self.c.fetchall())
        pass
    
    def criacaoGraficoVagasSul(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in the south
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')
        sd.graficoDVS(self, self.c.fetchall())
        pass
    
    def criacaoGraficoPermilagemNorte(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of ocuppied
            vacancies in the north
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')
        sd.graficoDPN(self, self.c.fetchall())
        pass
    
    def criacaoGraficoPermilagemCentro(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of ocuppied
            vacancies in the center
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')
        sd.graficoDPC(self, self.c.fetchall())
        pass
    
    def criacaoGraficoPermilagemSul(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of ocuppied
            vacancies in the south
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select * from distritos''')
        sd.graficoDPS(self, self.c.fetchall())
        pass
    
    def criacaoGraficoEscolasEntradas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in schools
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoEscolasEntradas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoEscolasVagas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in schools
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoEscolasVagas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoEscolasPercentagem(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of
            ocupied vacancies in schools
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoEscolasPercentagem(self, self.c.fetchall())
        pass
    
    def criacaoGraficoInstitutosEntradas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in institutes
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoInstitutosEntradas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoInstitutosVagas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in institutes
            @param ficheiro_base_de_dados name of the database
        """   
        self.c.execute('''select*from escolas''')
        sd.graficoInstitutosVagas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoInstitutosPercentagem(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of
            ocupied vacancies in institutes
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoInstitutosPercentagem(self, self.c.fetchall())
        pass
    
    def criacaoGraficoUniversidadesEntradas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of entries in
            universities
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoUniversidadesEntradas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoUniversidadesVagas(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the number of vacancies in
            universities
            @param ficheiro_base_de_dados name of the database
        """  
        self.c.execute('''select*from escolas''')
        sd.graficoUniversidadesVagas(self, self.c.fetchall())
        pass
    
    def criacaoGraficoUniversidadesPercentagem(self,ficheiro_base_de_dados):
        """
            Creates the query which will give the nedded information
            to make the graph which gives the per thousand of
            ocupied vacancies in univesities
            @param ficheiro_base_de_dados name of the database
        """
        self.c.execute('''select*from escolas''')
        sd.graficoUniversidadesPercentagem(self, self.c.fetchall())
        pass
