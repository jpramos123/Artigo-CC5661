from numpy.random import normal
import mysql.connector as con


class DataGenerator(object):
	def __init__(self):
		self.infected = {}

	def connection(self):
		cnx = con.connect(user='mvp',
						  password='epidemiologia',
						  host='johnny.heliohost.org',
						  database='mvp_viral')
		return cnx

	def iszero(self, num, alt):
		return alt if num == 0 else num

	def getPattern(self, classType):
		query = 'SELECT * FROM INFEC_TYPE WHERE id_infec = {}'.format(classType)
		cnx = self.connection()
		cursor = cnx.cursor()
		cursor.execute(query)
		infected = cursor.fetchall()[0]
		cursor.close()
		cnx.close()
		return infected

	def insert(self, infected):
		query = (" INSERT INTO INFECTED ("
				 " class_type,  ramo_ativ, genero,     vacinado,  sin_dor, dt_dor,  sin_hemo, dt_hemo,"
				 " sin_faget,   dt_faget,  sin_anuria, dt_anuria, sin_adv, exa_tgo, exa_tgp,  exa_bil, "
				 " class_final, evol_caso, est_final,  uf_prob)"
				 " VALUES "
				 " (%s")
		for i in range(0,19): query+=",%s"

		query+=")"

		cnx = self.connection()
		cursor = cnx.cursor()
		try:
			cursor.execute(query, infected)
			print('Infected successfully created!')
		except Exception as e:
			print(str(e))
		finally:
			cnx.close()
			cursor.close()

	def generateInfected(self, classType, noisePerc, quantity):
		# classType - Must be in [1,4]
		#	references the infected state:
		#	1 - Light | 2 - Medium | 3 - Severe | 4 - Malignant

		infecPattern = self.getPattern(classType)

		for i in range(quantity):
			newInfected = [infecPattern[0]]
			a = 0 # Remover no código final
			for j in range(1,len(infecPattern)):
				deviation = noisePerc * self.iszero(infecPattern[j], 1)
				newInfected.append(abs(normal(infecPattern[j], deviation)) % 1)
			self.insert(tuple(newInfected))


		# o dado vindo do select será o centro do numpy.random.normal
		# já o parâmetro noisePerc será o 'scale' --> Desvio Padrão

	def getInfectedList(self):
		query = ("SELECT class_type,  ramo_ativ,   genero,    vacinado,  sin_dor,  "
				 " 		 dt_dor,  	  sin_hemo,    dt_hemo,   sin_faget, dt_faget, "
				 " 		 sin_anuria,  dt_anuria,   sin_adv,   exa_tgo, 	 exa_tgp,  "
				 "		 exa_bil, 	  class_final, evol_caso, est_final, uf_prob   "
				 "FROM 	INFECTED")

		cnx = self.connection()
		cursor = cnx.cursor()
		try:
			cursor.execute(query)
			result = cursor.fetchall()
		except Exception as e:
			print(str(e))
		finally:
			cursor.close()
			cnx.close()

		return result