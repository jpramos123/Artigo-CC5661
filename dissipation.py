# -*- coding: utf-8 -*-
import numpy
from random import randint
from randDate import randomDateHot, randomDateCold, randomDateP
from numpy.random import choice

import mysql.connector as con


def getConnection():

	cnx = con.connect(	user='mvp',
						password='epidemiologia',
    		        	host='johnny.heliohost.org',
        		    	database='mvp_viral')

	return cnx

def end(cnx, cursor):
    cursor.close()
    cnx.close()


def formatInsert(table, dic):

	insert = "INSERT INTO " +table+" ("

	first = True
	for k,v in dic.items():
		if first:
			insert += str(k)
			first = False
		else:
			insert += ',' + str(k)

	insert += ") VALUES ( "

	first = True
	for k,v in dic.items():
		if first:
			insert += '%(' + str(k) + ')s'
			first = False
		else:
			insert += ',%(' + str(k) + ')s'
	insert += ")"

	return insert

def dispersao(outlier = 0):
	# Função para popular a tabela INFECTADOS
	def datefor(var, delta):
		if var and outlier:
			return randomDateP(infectado['dt_infec'], delta+randint(4,6))
		elif var:
			return randomDateP(infectado['dt_infec'], delta)
		else:
			return ''

	def mighthave(symp):
		if symp:
			return randint(0,1)
		elif outlier:
			return 1
		else:
			return 0

	def musthave(symp):
		if symp:
			if outlier:
				return 0
			else:
				return 1
		else:
			return randint(0,1)

	def evolucao():
		if not infectado['sin_dor']:
			return 1
		elif not infectado['sin_anuria']:
			return 2
		elif not infectado['sin_hemo']:
			return 3
		else:
			return 4

	def bigest_date():
		big = infectado['dt_dor']
		if infectado['dt_hemo']   > big: big = infectado['dt_hemo']
		if infectado['dt_faget']  > big: big = infectado['dt_faget']
		if infectado['dt_anuria'] > big: big = infectado['dt_anuria']
		if big == '': big = infectado['dt_infec']
		return randomDateP(big, 2)

	def death_odd():
		p_death = infectado['evol_caso'] / 5
		p_live = 1 - p_death
		p[0] = p_live
		p[1] = p_death

	def define_date():
		if outlier:
			return randomDateCold()
		return randomDateHot()

	def genero():
		if not outlier:
			return int(choice(numpy.arange(0, 2), p=[0.2, 0.8]))
		return int(choice(numpy.arange(0, 2), p=[0.8, 0.2]))

	def vacinado():
		if not outlier:
			return int(choice(numpy.arange(0, 2), p=[0.9, 0.1]))
		return int(choice(numpy.arange(0, 2), p=[0.1, 0.9]))

	def classificacao():
		if not outlier:
			return int(choice(numpy.arange(1,3), p=[0.2, 0.8]))
		return int(choice(numpy.arange(0, 2), p=[0.7, 0.3]))


	def get_uf():
		query = 'SELECT uf_prob FROM FED_UNITS'
		cnx = getConnection()
		cursor = cnx.cursor()
		cursor.execute(query)
		state_prob = cursor.fetchall()
		g = []

		for i in range(0,27):
			if outlier:
				if state_prob[i][0] > 0.0:
					state_prob[i] = 0.0
				else:
					state_prob[i] = 0.2
			else:
				state_prob[i] = state_prob[i][0]

		uf_id = float(choice(numpy.arange(1,28), p=state_prob))

		query = 'SELECT uf_prob, uf_id FROM FED_UNITS WHERE uf_id = {}'.format(uf_id)
		cursor.execute(query)
		result = cursor.fetchone()

		end(cnx, cursor)
		return {'uf_prob': result[0], 'uf_id': result[1]}


	infectado = {}
	p = []
	uf = get_uf()

	infectado['uf_id']	 	 = uf['uf_id']				 					  # uf_infec
	infectado['uf_prob']	 = uf['uf_prob']			 					  # uf_infec
	infectado['dt_infec']    = define_date()		    					  # dt_infec
	infectado['ramo_ativ']   = randint(1,5)      		    				  # ramo_ativ
	infectado['genero'] 	 = genero()										  # genero
	infectado['vacinado']    = vacinado()									  # vacinado
	infectado['sin_faget']   = randint(0,1)     		    				  # sin_faget
	infectado['dt_faget']    = datefor(infectado['sin_faget'],2)			  # dt_faget
	infectado['sin_dor']     = mighthave(infectado['sin_faget'])			  # sin_dor
	infectado['sin_anuria']  = mighthave(infectado['sin_dor'])  			  # sin_anuria
	infectado['sin_hemo']    = mighthave(infectado['sin_anuria'])			  # sin_hemo
	infectado['dt_dor']      = datefor(infectado['sin_dor'], randint(2,3))    # dt_dor
	infectado['dt_anuria']   = datefor(infectado['sin_anuria'], randint(3,5)) # dt_anuria
	infectado['dt_hemo']     = datefor(infectado['sin_hemo'], randint(6,12))  # dt_hemo
	infectado['sin_adv']     = randint(0,1)      							  # sin_adv
	infectado['desc_sinadv'] = 'NULL'             							  # desc_sinadv
	infectado['exa_tgo']     = musthave(infectado['sin_anuria'])			  # exa_tgo
	infectado['exa_tgp']     = musthave(infectado['sin_anuria'])			  # exa_tgp
	infectado['exa_bil']     = musthave(infectado['sin_hemo'])				  # exa_bil
	infectado['class_final'] = classificacao()     							  # class_final
	infectado['evol_caso']	 = evolucao()									  # evol_caso
	infectado['est_final']	 = int(choice(numpy.arange(0, 2),
								   p=[1-infectado['evol_caso'] / 5,
										infectado['evol_caso'] / 5]))		  # est_final
	infectado['dt_enc']		 = bigest_date()								  # dt_enc
	infectado['outlier']	 = outlier										  # outlier

	insert_infectado = formatInsert('INFECTADOS', infectado)
	#print insert_infectado

	cnx = getConnection()
	cursor = cnx.cursor()
	try:
		cursor.execute(insert_infectado, infectado)
		print ('Registro inserido com sucesso!')
	except Exception as e:
		print ('ERRO!' + str(e))
	except Exception as e:
			print ('ERRO!{0}'.frt_infecormat(str(e)))
	end(cnx, cursor)
	return infectado


def dispersao(outlier=0):
	# Função para popular a tabela INFECTADOS
    def datefor(var, delta):
        if var and outlier:
            return randomDateP(infectado['dt_infec'], delta + randint(4, 6))
        elif var:
            return randomDateP(infectado['dt_infec'], delta)
        else:
            return ''

    def mighthave(symp):
        if symp:
            return randint(0, 1)
        elif outlier:
            return 1
        else:
            return 0

    def musthave(symp):
        if symp:
            if outlier:
                return 0
            else:
                return 1
        else:
            return randint(0, 1)

    def evolucao():
        if not infectado['sin_dor']:
            return 1
        elif not infectado['sin_anuria']:
            return 2
        elif not infectado['sin_hemo']:
            return 3
        else:
            return 4

    def bigest_date():
        big = infectado['dt_dor']
        if infectado['dt_hemo'] > big: big = infectado['dt_hemo']
        if infectado['dt_faget'] > big: big = infectado['dt_faget']
        if infectado['dt_anuria'] > big: big = infectado['dt_anuria']
        if big == '': big = infectado['dt_infec']
        return randomDateP(big, 2)

    def death_odd():
        p_death = infectado['evol_caso'] / 5
        p_live = 1 - p_death
        p[0] = p_live
        p[1] = p_death

    def define_date():
        if outlier:
            return randomDateCold()
        return randomDateHot()

    def genero():
        if not outlier:
            return int(choice(numpy.arange(0, 2), p=[0.2, 0.8]))
        return int(choice(numpy.arange(0, 2), p=[0.8, 0.2]))

    def vacinado():
        if not outlier:
            return int(choice(numpy.arange(0, 2), p=[0.9, 0.1]))
        return int(choice(numpy.arange(0, 2), p=[0.1, 0.9]))

    def classificacao():
        if not outlier:
            return int(choice(numpy.arange(1, 3), p=[0.2, 0.8]))
        return int(choice(numpy.arange(0, 2), p=[0.7, 0.3]))

    def get_uf():
        query = 'SELECT uf_prob FROM FED_UNITS'
        cnx = getConnection()
        cursor = cnx.cursor()
        cursor.execute(query)
        state_prob = cursor.fetchall()
        g = []

        for i in range(0, 27):
            if outlier:
                if state_prob[i][0] > 0.0:
                    state_prob[i] = 0.0
                else:
                    state_prob[i] = 0.2
            else:
                state_prob[i] = state_prob[i][0]

        uf_id = float(choice(numpy.arange(1, 28), p=state_prob))

        query = 'SELECT uf_prob, uf_id FROM FED_UNITS WHERE uf_id = {}'.format(uf_id)
        cursor.execute(query)
        result = cursor.fetchone()

        end(cnx, cursor)
        return {'uf_prob': result[0], 'uf_id': result[1]}

    infectado = {}
    p = []
    uf = get_uf()

    infectado['uf_id'] = uf['uf_id']  # uf_infec
    infectado['uf_prob'] = uf['uf_prob']  # uf_infec
    infectado['dt_infec'] = define_date()  # dt_infec
    infectado['ramo_ativ'] = randint(1, 5)  # ramo_ativ
    infectado['genero'] = genero()  # genero
    infectado['vacinado'] = vacinado()  # vacinado
    infectado['sin_faget'] = randint(0, 1)  # sin_faget
    infectado['dt_faget'] = datefor(infectado['sin_faget'], 2)  # dt_faget
    infectado['sin_dor'] = mighthave(infectado['sin_faget'])  # sin_dor
    infectado['sin_anuria'] = mighthave(infectado['sin_dor'])  # sin_anuria
    infectado['sin_hemo'] = mighthave(infectado['sin_anuria'])  # sin_hemo
    infectado['dt_dor'] = datefor(infectado['sin_dor'], randint(2, 3))  # dt_dor
    infectado['dt_anuria'] = datefor(infectado['sin_anuria'], randint(3, 5))  # dt_anuria
    infectado['dt_hemo'] = datefor(infectado['sin_hemo'], randint(6, 12))  # dt_hemo
    infectado['sin_adv'] = randint(0, 1)  # sin_adv
    infectado['desc_sinadv'] = 'NULL'  # desc_sinadv
    infectado['exa_tgo'] = musthave(infectado['sin_anuria'])  # exa_tgo
    infectado['exa_tgp'] = musthave(infectado['sin_anuria'])  # exa_tgp
    infectado['exa_bil'] = musthave(infectado['sin_hemo'])  # exa_bil
    infectado['class_final'] = classificacao()  # class_final
    infectado['evol_caso'] = evolucao()  # evol_caso
    infectado['est_final'] = int(choice(numpy.arange(0, 2),
                                        p=[1 - infectado['evol_caso'] / 5,
                                           infectado['evol_caso'] / 5]))  # est_final
    infectado['dt_enc'] = bigest_date()  # dt_enc
    infectado['outlier'] = outlier  # outlier

    insert_infectado = formatInsert('INFECTADOS', infectado)
    # print insert_infectado

    cnx = getConnection()
    cursor = cnx.cursor()
    try:
        cursor.execute(insert_infectado, infectado)
        print('Registro inserido com sucesso!')
    except Exception as e:
        print('ERRO!{0}'.format(str(e)))
    end(cnx, cursor)
    return infectado
