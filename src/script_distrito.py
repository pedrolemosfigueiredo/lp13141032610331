# -*- coding: utf-8 -*-

import sqlite3
import matplotlib.pyplot as graf
import numpy as np

def tabela_distritos(lista):
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
		
		
'''try:
			print info + ' =) ' + distrito
			print "distrito de " + mapa_distritos[distrito]
		except:
			print info + ' =) ' + distrito
			pass
		pass'''
'''
	 cursor.commit()
	 conn.close()
	 '''
	 


def tabela_escolas(lista):
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
'''def graficoInst(mother, lista):
        tamanho = len(lista)
        arrayInstituicao = []
        arrayEntradas = []
        for row in lista:
                arrayInstituicao.append(row[0])
                'arrayEntradas.append(row[1])'
                print row[1]
                pass
        graf.xlabel = 'instituições'
        graf.ylable = 'entradas'
        graf.plot(arrayInstituicao, arrayEntradas)
        graf.show()
	'''
