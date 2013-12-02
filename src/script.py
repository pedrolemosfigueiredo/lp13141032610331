# -*- coding: utf-8 -*-

import sqlite3
import matplotlib.pyplot as graf
import numpy as np

"""
        This script is the logic segment of this program, in a MVC
        comparison this would be the section most similar to the model
"""
def tabela_distritos(lista):
        """
                This function creates the district table on the database and
                inserts the values into it
                @param lista the list with districts on the resultados_rna table
        """
	mapa_distritos = { 'Lisboa' : 'Lisboa' }
	conn = sqlite3.connect('trabalho')
	conn.text_factory = str
	cursor = conn.cursor()
	cursor.execute("drop table if exists distritos")
	cursor.execute('''create table distritos
			(distrito, entradas, vagas, permilagem)                        
			''')
	conn.commit()
	distritos = ['Aveiro','Beja','Braga','Bragança',
	'Castelo Branco', 'Coimbra', 'Évora','Faro','Guarda','Leiria',
	'Lisboa','Portalegre','Porto','Santarém','Setúbal',
	'Viana do Castelo','Vila Real', 'Viseu']
	escola = ""
	entradas = 0
	vagas = 0
	data = []
	for distrito in distritos:
		for row in lista:
			if distrito in row[0]:
				if distrito != 'Braga':
					entradas += row[1]
					vagas += row[2]
				pass
			if distrito == 'Faro':
				if 'Algarve' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				pass
			if distrito == 'Vila Real':
				if 	'Beira Interior' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				if 	'Alto Douro' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass				
				pass
			if distrito == 'Braga':
				if 	'Minho' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				if 'cávado' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				pass
			if distrito == 'Santarém':
				if 'Tomar' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				pass	
			if distrito == 'Lisboa':
				if 'ISCTE' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				if 'Infante D. Henrique' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				if 'Hotelaria e Turismo' in row[0]:
					entradas += row[1]
					vagas  += row[2]
					pass
				pass	
		data.append([distrito,entradas,vagas, (entradas * 1000.0/(entradas+vagas))])
		entradas = 0
		vagas = 0
		pass
	for x in data:
		cursor.execute('insert into distritos values(?,?,?,?)',(x[0],x[1],x[2], x[3]))
		pass
	conn.commit()

	 


def tabela_escolas(lista):
        """
                This function creates the schools table on the database and
                inserts the values into it
                @param lista the list with schools on the resultados_rna table
        """
        conn = sqlite3.connect('trabalho')
        conn.text_factory = str
	cursor = conn.cursor()
	cursor.execute("drop table if exists escolas")
	cursor.execute('''create table escolas(instituição , entradas, vagas, 
			percentagem)''')
	conn.commit()
	entry = 0
	position = 0
	totalEntradas = 0
	r = ""
	data = []
	totalDeAlunos = 0
	for row in lista:
		totalDeAlunos += row[6]
		pass
	relacao = 0.0
	
	for row in lista:
		if(r == row[2].split(' - ')[0]):
			entry += row[6]
			position += row[8]
			relacao += (row[6] * 100.0)/totalDeAlunos
			pass
		else:
			data.append([r, entry, position, relacao])
			r = row[2].split(' - ')[0]
			entry = row[6]
			position = row[8]
			relacao = ((row[6] *100.0)/totalDeAlunos) + 0.0
			pass
		totalEntradas += entry
		pass
	contador = 0
	for dados1 in data:
		for dados2 in data:
			if dados1 != dados2:
				if dados1[0] == dados2[0]:
					dados1[1] += dados2[1]
					dados1[2] += dados2[2]
					dados1[3] += dados2[3]
					data.pop(contador)
					pass
				pass
			contador += 1
			pass
		contador = 0
		pass
					
	'''for institution in data:
		if institution[0] == row[2].split(' - ')[0]:
			institution[1] += entry
			institution[2] += position'''
	data.pop(0)
	for x in data:
		cursor.execute('insert into escolas values(?,?,?,?);',(x[0], x[1], x[2], x[3]))
		pass
	conn.commit()
	pass
#Constrói um gráfico que demonstra o nº de alunos colocados por 
#instituição

def graficoInst(mother, lista):
        """
                Builds a graphic wich demonstrates the number of students
                positioned in each instituicion
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayEntradas = []
	for row in lista:
		arrayInstituicao.append(row[0])
		arrayEntradas.append(row[1])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Entradas em instituições')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass 
	
#Constrói um gráfico que demonstra o nº de vagas sobrantes por 
#instituição

def graficoIV(mother, lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in each instituicion
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayVagas = []
	for row in lista:
		arrayInstituicao.append(row[0])
		arrayVagas.append(row[2])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao) - 1)
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('vagas')
	ax.set_title(u'Vagas em instituições')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	graf.bar(x, arrayVagas)
	graf.show()
	print arrayVagas
	pass

# Constrói o Gráfico das estatísticas que mostra a percentagem de alunos
# numa instituição em relação ao total de alunos

def graficoIP(mother, lista):
        """
                Builds a graphic wich demonstrates the per thousand of ocuppied
                vacancies in each instituicion
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayPercentagem = []
	for row in lista:
		arrayInstituicao.append(row[0])
		arrayPercentagem.append(row[3])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao) - 1)
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('Percentagem')
	ax.set_title(u'Percentagem de alunos em relação ao total')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	graf.bar(x, arrayPercentagem)
	graf.show()
	pass
# Constrói um gráfico que mostra os alunos colocados por distrito
def graficoDA(mother,lista):
        """
                Builds a graphic wich demonstrates the number of students
                positioned in each district
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayAluno = [],[]
	for row in lista:
		arrayDistrito.append(row[0])
		arrayAluno.append(row[1])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('alunos')
	ax.set_title('Alunos colocados por distrito')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayAluno)
	graf.show()
	pass
#Constrói um gráfico que mostra as vagas sobrantes po distrito
def graficoDV(mother,lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in each district
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayVaga = [],[]
	for row in lista:
		arrayDistrito.append(row[0])
		arrayVaga.append(row[2])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayVDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('vagas')
	ax.set_title('Vagas sobrantes por distrito')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayVaga)
	graf.show()
	pass
# Constrói um gráfico que mostra em permilagem os alunos que 
# entraram em relação àqueles que concorreram por distrito
def graficoDP(mother,lista):
        """
                Builds a graphic wich demonstrates the per thousand of ocuppied
                vacancies in each district
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayPermilagem = [],[]
	for row in lista:
		arrayDistrito.append(row[0])
		arrayPermilagem.append(row[3])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('permilagem')
	ax.set_title('Permilagem de alunos colocados por distrito')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayPermilagem)
	graf.show()
	pass

def graficoDEN(mother,lista):
        """
                Builds a graphic wich demonstrates the number entrys
                in the north
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayEntradas = [],[]
	for row in lista:
		if ((row[0] == 'Braga') | (row[0] == 'Vila Real') |
		(row[0] == 'Aveiro') | (row[0] == 'Bragança') | (row[0] == 'Coimbra')|
		(row[0] == 'Guarda') | (row[0] == 'Porto') | (row[0] == 'Viseu')):
			arrayDistrito.append(row[0])
			arrayEntradas.append(row[1])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Alunos colocados por distrito no Norte')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoDEC(mother,lista):
        """
                Builds a graphic wich demonstrates the number entrys
                in the center
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayEntradas = [],[]
	print 'olá'
	for row in lista:
		if ((row[0] == 'Lisboa') | (row[0] == 'Leiria') |
		(row[0] == 'Santarém') | (row[0] == 'Castelo Branco') | 
		(row[0] == 'Setúbal') | (row[0] == 'Portalegre')):
			arrayDistrito.append(row[0])
			arrayEntradas.append(row[1])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Alunos colocados por distrito no Centro')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoDES(mother,lista):
        """
                Builds a graphic wich demonstrates the number entrys
                in the south
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayEntradas = [],[]
	for row in lista:
		if ((row[0] == 'Faro') | (row[0] == 'Évora') |
		(row[0] == 'Beja')):
			arrayDistrito.append(row[0])
			arrayEntradas.append(row[1])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Alunos colocados por distrito no Sul')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoDVN(mother,lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in the north
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayVagas = [],[]
	for row in lista:
		if ((row[0] == 'Braga') | (row[0] == 'Vila Real') |
		(row[0] == 'Aveiro') | (row[0] == 'Bragança') | (row[0] == 'Coimbra')|
		(row[0] == 'Guarda') | (row[0] == 'Porto') | (row[0] == 'Viseu')):
			arrayDistrito.append(row[0])
			arrayVagas.append(row[2])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Vagas sobrantes por distrito no Sul')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoDVC(mother,lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in the center
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayVagas = [],[]
	print 'olá'
	for row in lista:
		if ((row[0] == 'Lisboa') | (row[0] == 'Leiria') |
		(row[0] == 'Santarém') | (row[0] == 'Castelo Branco') | 
		(row[0] == 'Setúbal') | (row[0] == 'Portalegre')):
			arrayDistrito.append(row[0])
			arrayVagas.append(row[2])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Alunos colocados por distrito no Centro')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoDVS(mother,lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in the south
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayVagas = [],[]
	for row in lista:
		if ((row[0] == 'Faro') | (row[0] == 'Évora') |
		(row[0] == 'Beja')):
			arrayDistrito.append(row[0])
			arrayVagas.append(row[2])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Alunos colocados por distrito no Sul')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoDPN(mother,lista):
        """
                Builds a graphic wich demonstrates the per thousand
                of ocuppied vacancies in the north
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayPermilagem = [],[]
	for row in lista:
		if ((row[0] == 'Braga') | (row[0] == 'Vila Real') |
		(row[0] == 'Aveiro') | (row[0] == 'Bragança') | (row[0] == 'Coimbra')|
		(row[0] == 'Guarda') | (row[0] == 'Porto') | (row[0] == 'Viseu')):
			arrayDistrito.append(row[0])
			arrayPermilagem.append(row[3])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Permilagem de alunos colocados por distrito no Norte')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayPermilagem)
	graf.show()
	pass

def graficoDPC(mother,lista):
        """
                Builds a graphic wich demonstrates the per thousand
                of ocuppied vacancies in the center
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayPermilagem = [],[]
	for row in lista:
		if ((row[0] == 'Lisboa') | (row[0] == 'Leiria') |
		(row[0] == 'Santarém') | (row[0] == 'Castelo Branco') | 
		(row[0] == 'Setúbal') | (row[0] == 'Portalegre')):
			arrayDistrito.append(row[0])
			arrayPermilagem.append(row[3])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Permilagem de alunos colocados por distrito no Centro')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayPermilagem)
	graf.show()
	pass

def graficoDPS(mother,lista):
        """
                Builds a graphic wich demonstrates the per thousand
                of ocuppied vacancies in the south
                @param lista list with the number of students in the institutes
        """
	arrayDistrito, arrayPermilagem = [],[]
	for row in lista:
		if ((row[0] == 'Faro') | (row[0] == 'Évora') |
		(row[0] == 'Beja')):
			arrayDistrito.append(row[0])
			arrayPermilagem.append(row[3])
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayDistrito))
	ax.set_xlabel('distritos')
	ax.set_ylabel('Entradas')
	ax.set_title('Permilagem de alunos colocados por distrito no Sul')
	ax.set_xticklabels(zip(arrayDistrito), rotation = 90)
	ax.bar(x, arrayPermilagem)
	graf.show()
	pass

def graficoEscolasEntradas(mother, lista):
        """
                Builds a graphic wich demonstrates the number of entrys
                in each school
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayEntradas = []
	for row in lista:
		if 'Escola' in row[0]:
			arrayInstituicao.append(detectUpper(row[0]))
			arrayEntradas.append(row[1])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Entradas em escolas')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoEscolasVagas(mother, lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in each school
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayVagas = []
	for row in lista:
		if 'Escola' in row[0]:
			arrayInstituicao.append(detectUpper(row[0]))
			arrayVagas.append(row[2])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'vagas em escolas')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	print arrayVagas
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoEscolasPercentagem(mother, lista):
        """
                Builds a graphic wich demonstrates the per thousand of ocuppied
                vacancies in each school
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayPercentagem = []
	for row in lista:
		if 'Escola' in row[0]:
			arrayInstituicao.append(detectUpper(row[0]))
			arrayPercentagem.append(row[3])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Percentagem de alunos em relação ao total')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayPercentagem)
	graf.show()
	pass

def graficoInstitutosEntradas(mother, lista):
        """
                Builds a graphic wich demonstrates the number of entrys
                in each institute
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayEntradas = []
	for row in lista:
		if (('Instituto' in row[0])|('ISCTE' in row[0])):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayEntradas.append(row[1])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Entrada de alunos em institutos')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoInstitutosVagas(mother, lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in each institute
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayVagas = []
	for row in lista:
		if (('Instituto' in row[0])|('ISCTE' in row[0])):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayVagas.append(row[2])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'vagas em institutos')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoInstitutosPercentagem(mother, lista):
        """
                Builds a graphic wich demonstrates the per thousand of ocuppied
                vacancies in each institute
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayPercentagem = []
	for row in lista:
		if (('Instituto' in row[0])|('ISCTE' in row[0])):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayPercentagem.append(row[3])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Percentagem de alunos em relação ao total')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayPercentagem)
	graf.show()
	pass

def graficoUniversidadesEntradas(mother,lista):
        """
                Builds a graphic wich demonstrates the number of students
                positioned in each university
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayEntradas = []
	for row in lista:
		if (('Universidade') in row[0]):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayEntradas.append(row[1])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'entradas de alunos em universidades')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayEntradas)
	graf.show()
	pass

def graficoUniversidadesVagas(mother,lista):
        """
                Builds a graphic wich demonstrates the number of vacancies
                in each university
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayVagas = []
	for row in lista:
		if (('Universidade') in row[0]):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayVagas.append(row[2])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'vagas em universidades')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayVagas)
	graf.show()
	pass

def graficoUniversidadesPercentagem(mother,lista):
        """
                Builds a graphic wich demonstrates the per thousand of ocuppied
                vacancies in each university
                @param lista list with the number of students in the institutes
        """
	arrayInstituicao = []
	arrayPercentagem = []
	for row in lista:
		if (('Universidade') in row[0]):
			arrayInstituicao.append(detectUpper(row[0]))
			arrayPercentagem.append(row[3])
			pass
		pass
	figs, ax = graf.subplots()
	x = np.arange(len(arrayInstituicao))
	ax.set_xlabel(u'instituições')
	ax.set_ylabel('entradas')
	ax.set_title(u'Percentagens de aluno em relação ao total')
	ax.set_xticklabels(zip(arrayInstituicao), rotation = 90)
	ax.bar(x, arrayPercentagem)
	graf.show()
	pass
	
def detectUpper(x):
	b = ''
	for letter in x:
		if letter.isupper() == True:
			b += letter
			pass
		pass
	return b
	pass
