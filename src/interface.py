#!/usr/bin/env python
# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo e Alexandre Leitão
# data: 30 de Setembro de 2013
# trabalho de Linguagens de Programação
# generated by wxGlade 0.6.5 on Thu Nov 28 19:38:25 2013

import wx
import trabalho as t
# begin wxGlade: extracode
# end wxGlade
"""
This is the interface class, once you start the program by initializing
this class
"""

class MyFrame(wx.Frame):
        """
                Starts the the program interface
                @param wx.Frame The window of the program 
        """
        
	def __init__(self, *args, **kwds):
                """
                        Constructor method of the wx interface                        
                """
		# begin wxGlade: MyFrame.__init__
		self.tr =t.Trabalho()
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		
		self.notebook_1 = wx.Notebook(self, -1, style=0)# Creates the section where all the panes will be deposited
		
		self.notebook_1_pane_db = wx.Panel(self.notebook_1, -1)# Creates the first pane which contains 3 buttons responsible for creating the DB, CSVs and imports data from xls 
		self.label_1 = wx.StaticText(self.notebook_1_pane_db, -1, u"Clicando no botão seguinte pode fazer a passagem dos dados da folha excel para uma base de dados")
		
		self.button_criar_db = wx.Button(self.notebook_1_pane_db, -1, "Criar Base de dados")
		self.Bind(wx.EVT_BUTTON, self.criar_db, self.button_criar_db)
		
		self.label_2 = wx.StaticText(self.notebook_1_pane_db, -1, u"Clicando no botão seguinte cria duas tabelas. Uma com as estatísticas das escolas e outra com as estatísticas dos distritos.")
		
		self.button_estatisticas = wx.Button(self.notebook_1_pane_db, -1, u"Criação de tabelas para a estatística")
		self.Bind(wx.EVT_BUTTON, self.criar_estatisticas, self.button_estatisticas)
		self.label_csv = wx.StaticText(self.notebook_1_pane_db, -1, u"Clicando no botão seguinte passa os dados da estatística para um ficheiro CSV")
		self.button_csv = wx.Button(self.notebook_1_pane_db, -1, u"Criar ficheiro CSV")
		self.Bind(wx.EVT_BUTTON, self.passagem_csv, self.button_csv)
		
		self.notebook_1_pane_graficos_distritos = wx.Panel(self.notebook_1, -1)
		self.label_3 = wx.StaticText(self.notebook_1_pane_graficos_distritos, -1, u"Criação das estatísticas dos institutos do Norte")
		
		self.button_entradas_norte = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_norte, self.button_entradas_norte)
		
		self.button_vagas_norte = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_norte, self.button_vagas_norte)
		
		self.button_permilagem_norte = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "permilagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_permilagem_norte, self.button_permilagem_norte)
		
		self.static_line_1 = wx.StaticLine(self.notebook_1_pane_graficos_distritos, -1, style=wx.LI_VERTICAL)
		self.label_4 = wx.StaticText(self.notebook_1_pane_graficos_distritos, -1, u"Criação das estatísticas dos institutos do Centro")
		
		self.button_entradas_centro = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_centro, self.button_entradas_centro)
		
		self.button_vagas_centro = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_centro, self.button_vagas_centro)
		
		self.button_permilagem_centro = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "permilagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_permilagem_centro, self.button_permilagem_centro)
		
		self.static_line_2 = wx.StaticLine(self.notebook_1_pane_graficos_distritos, -1, style=wx.LI_VERTICAL)
		self.label_5 = wx.StaticText(self.notebook_1_pane_graficos_distritos, -1, u"Criação das estatísticas do Sul")
		
		self.button_entradas_sul = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_sul, self.button_entradas_sul)
		
		self.button_vagas_sul = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_sul, self.button_vagas_sul)
		
		self.button_permilagem_sul = wx.Button(self.notebook_1_pane_graficos_distritos, -1, "permilagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_permilagem_Sul, self.button_permilagem_sul)
		
		self.notebook_1_pane_graficos_intituicoes = wx.Panel(self.notebook_1, -1)
		self.label_6 = wx.StaticText(self.notebook_1_pane_graficos_intituicoes, -1, u"Criação do gráfico das escolas")
		
		self.button_entradas_escolas = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_escolas, self.button_entradas_escolas)
		
		self.button_vagas_escolas = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_escolas, self.button_vagas_escolas)
		
		self.button_percentagem_escolas = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "percentagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_percentagem_escolas, self.button_percentagem_escolas)
		
		self.static_line_3 = wx.StaticLine(self.notebook_1_pane_graficos_intituicoes, -1, style=wx.LI_VERTICAL)
		self.label_7 = wx.StaticText(self.notebook_1_pane_graficos_intituicoes, -1, u"Criação do gráfico dos politécnicos")
		
		self.button_entradas_politecnicos = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_institutos, self.button_entradas_politecnicos)
		
		self.button_vagas_politecnicos = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_institutos, self.button_vagas_politecnicos)
		
		self.button_percentagem_politecnicos = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "percentagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_percentagem_institutos, self.button_percentagem_politecnicos)
		
		self.static_line_4 = wx.StaticLine(self.notebook_1_pane_graficos_intituicoes, -1, style=wx.LI_VERTICAL)
		self.label_8 = wx.StaticText(self.notebook_1_pane_graficos_intituicoes, -1, u"criação do gráfico das universidades")
		
		self.button_entradas_universidades = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "entradas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_entradas_universidades, self.button_entradas_universidades)
		
		self.button_vagas_universidades = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "vagas")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_vagas_universidades, self.button_vagas_universidades)
		
		self.button_percentagem_universidades = wx.Button(self.notebook_1_pane_graficos_intituicoes, -1, "percentagem")
		self.Bind(wx.EVT_BUTTON, self.criar_grafico_percentagem_universidades, self.button_percentagem_universidades)
		
		self.__set_properties()
		self.__do_layout()
		
		# end wxGlade
		pass
#início de funções eventos dos botões.......................................................................    
	def criar_db(self, event):
                """
                        Event responsible for creating the DB
                """
		self.tr.passagem_de_dados('cna131fresultados.xls', 'trabalho')
		event.Skip()
		pass
	
	def criar_estatisticas(self, event):
                """
                        Event responsible for creating the estatistics in which the program is going to base himself
                """
		self.tr.estatistica1('trabalho')
		self.tr.estatistica2('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_norte(self, event):
                """
                        Event Responsible for creating the graph which shows the number of entries in the north
                """
		self.tr.criacaoGraficoEntradasNorte('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_centro(self, event):
                """
                     Event Responsible for creating the graph which shows the number of entries in the center   
                """
		self.tr.criacaoGraficoEntradasCentro('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_sul(self, event):
                """
                     Event Responsible for creating the graph which shows the number of entries in the south   
                """
		self.tr.criacaoGraficoEntradasSul('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_norte(self, event):
                """
                     Event Responsible for creating the graph which shows the number of vacancies in the north   
                """
		self.tr.criacaoGraficoVagasNorte('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_centro(self, event):
                """
                     Event Responsible for creating the graph which shows the number of vacancies in the center   
                """
		self.tr.criacaoGraficoVagasCentro('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_sul(self, event):
                """
                     Event Responsible for creating the graph which shows the number of vacancies in the south   
                """
		self.tr.criacaoGraficoVagasSul('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_permilagem_norte(self,event):
                """
                     Event Responsible for creating the graph which shows per thousand of vacancies ocuppied in the north  
                """
		self.tr.criacaoGraficoPermilagemNorte('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_permilagem_centro(self,event):
                """
                     Event Responsible for creating the graph which shows per thousand of vacancies ocuppied in the center  
                """
		self.tr.criacaoGraficoPermilagemCentro('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_permilagem_Sul(self,event):
                """
                     Event Responsible for creating the graph which shows per thousand of vacancies ocuppied in the south  
                """
		self.tr.criacaoGraficoPermilagemSul('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_escolas(self,event):
                """
                        Event resposible for creating the graph which links the number of entries in each school
                """
		self.tr.criacaoGraficoEscolasEntradas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_escolas(self,event):
                """
                        Event resposible for creating the graph which links the number of vacancies in each school
                """
		self.tr.criacaoGraficoEscolasVagas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_percentagem_escolas(self,event):
                """
                     Event Responsible for creating the graph which shows percentage of vacancies ocuppied in each school  
                """
		self.tr.criacaoGraficoEscolasPercentagem('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_institutos(self,event):
                """
                        Event resposible for creating the graph which links the number of entries in each institute
                """
		self.tr.criacaoGraficoInstitutosEntradas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_institutos(self,event):
                """
                        Event resposible for creating the graph which links the number of vacancies in each institute
                """
		self.tr.criacaoGraficoInstitutosVagas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_percentagem_institutos(self,event):
                """
                        Event resposible for creating the graph which shows percentage of vacancies ocuppied in each institute
                """
		self.tr.criacaoGraficoInstitutosPercentagem('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_entradas_universidades(self,event):
                """
                        Event resposible for creating the graph which links the number of entries in each university
                """
		self.tr.criacaoGraficoUniversidadesEntradas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_vagas_universidades(self,event):
                """
                        Event resposible for creating the graph which links the number of vacancies in each university
                """
		self.tr.criacaoGraficoUniversidadesVagas('trabalho')
		event.Skip()
		pass
	
	def criar_grafico_percentagem_universidades(self,event):
                """
                        Event resposible for creating the graph which shows percentage of vacancies ocuppied in each university
                """
		self.tr.criacaoGraficoUniversidadesPercentagem('trabalho')
		event.Skip()
		pass
	
	def passagem_csv(self,event):
                """
                        Event responsible for converting the database tables into csv files
                """
		self.tr.estatisticasCSV('trabalho')
		pass
	
#fim de funções eventos dos botões
	def __set_properties(self):
                """
                        This method sets important characteristics of the program interface frame
                """
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle(u"Trabalho prático")
		self.notebook_1_pane_graficos_distritos.SetMinSize((1302, 121))
		pass
		# end wxGlade

	def __do_layout(self):
                """
                        Sets the layout of the various elements within the frame
                """
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_21 = wx.BoxSizer(wx.VERTICAL)
		sizer_20 = wx.BoxSizer(wx.VERTICAL)
		sizer_19 = wx.BoxSizer(wx.VERTICAL)
		sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_13 = wx.BoxSizer(wx.VERTICAL)
		sizer_12 = wx.BoxSizer(wx.VERTICAL)
		sizer_9 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_6 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.label_1, 0, 0, 0)
		sizer_6.Add(self.button_criar_db, 0, 0, 0)
		sizer_6.Add(self.label_2, 0, 0, 0)
		sizer_6.Add(self.button_estatisticas, 0, 0, 0)
		sizer_6.Add(self.label_csv)
		sizer_6.Add(self.button_csv)
		sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)
		self.notebook_1_pane_db.SetSizer(sizer_2)
		sizer_9.Add(self.label_3, 0, 0, 0)
		sizer_9.Add(self.button_entradas_norte, 0, 0, 0)
		sizer_9.Add(self.button_vagas_norte, 0, 0, 0)
		sizer_9.Add(self.button_permilagem_norte, 0, 0, 0)
		sizer_8.Add(sizer_9, 1, wx.EXPAND, 0)
		sizer_10.Add(self.static_line_1, 0, wx.EXPAND, 0)
		sizer_12.Add(self.label_4, 0, 0, 0)
		sizer_12.Add(self.button_entradas_centro, 0, 0, 0)
		sizer_12.Add(self.button_vagas_centro, 0, 0, 0)
		sizer_12.Add(self.button_permilagem_centro, 0, 0, 0)
		sizer_11.Add(sizer_12, 1, wx.EXPAND, 0)
		sizer_11.Add(self.static_line_2, 0, wx.EXPAND, 0)
		sizer_13.Add(self.label_5, 0, 0, 0)
		sizer_13.Add(self.button_entradas_sul, 0, 0, 0)
		sizer_13.Add(self.button_vagas_sul, 0, 0, 0)
		sizer_13.Add(self.button_permilagem_sul, 0, 0, 0)
		sizer_11.Add(sizer_13, 1, wx.EXPAND, 0)
		sizer_10.Add(sizer_11, 1, wx.EXPAND, 0)
		sizer_8.Add(sizer_10, 1, wx.EXPAND, 0)
		sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
		self.notebook_1_pane_graficos_distritos.SetSizer(sizer_7)
		sizer_19.Add(self.label_6, 0, 0, 0)
		sizer_19.Add(self.button_entradas_escolas, 0, 0, 0)
		sizer_19.Add(self.button_vagas_escolas, 0, 0, 0)
		sizer_19.Add(self.button_percentagem_escolas, 0, 0, 0)
		sizer_18.Add(sizer_19, 1, wx.EXPAND, 0)
		sizer_18.Add(self.static_line_3, 0, wx.EXPAND, 0)
		sizer_20.Add(self.label_7, 0, 0, 0)
		sizer_20.Add(self.button_entradas_politecnicos, 0, 0, 0)
		sizer_20.Add(self.button_vagas_politecnicos, 0, 0, 0)
		sizer_20.Add(self.button_percentagem_politecnicos, 0, 0, 0)
		sizer_18.Add(sizer_20, 1, wx.EXPAND, 0)
		sizer_18.Add(self.static_line_4, 0, wx.EXPAND, 0)
		sizer_21.Add(self.label_8, 0, 0, 0)
		sizer_21.Add(self.button_entradas_universidades, 0, 0, 0)
		sizer_21.Add(self.button_vagas_universidades, 0, 0, 0)
		sizer_21.Add(self.button_percentagem_universidades, 0, 0, 0)
		sizer_18.Add(sizer_21, 1, wx.EXPAND, 0)
		self.notebook_1_pane_graficos_intituicoes.SetSizer(sizer_18)
		self.notebook_1.AddPage(self.notebook_1_pane_db, "base de dados")
		self.notebook_1.AddPage(self.notebook_1_pane_graficos_distritos, u"gráficos dos distritos")
		self.notebook_1.AddPage(self.notebook_1_pane_graficos_intituicoes, u"gráficos das instituições")
		sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade
		pass   

# end of class MyFrame
if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
	pass
	
