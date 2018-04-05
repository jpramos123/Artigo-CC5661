from numpy.random import normal
from numpy import asarray
import mysql.connector as con

class DataGenerator(object):
	def __init__(self):
		self.infected = {}
		self.cnx = self.connection()
		self.cursor = self.cnx.cursor()

	def connection(self):
		cnx = con.connect(user='mvp',
						  password='epidemiologia',
						  host='johnny.heliohost.org',
						  database='mvp_viral')
		return cnx

	def iszero(self, num, alt):
		return alt if num == 0 else num

	def tooBig(self, value):
		return 1 if value > 1 else value

	def tooSmall(self, value):
		return 0 if value < 0 else value

	def getPattern(self, classType):
		query = 'SELECT * FROM INFEC_TYPE WHERE id_infec = {}'.format(classType)
		self.cursor.execute(query)
		infected = self.cursor.fetchall()[0]
		return infected

	def insert(self, infected, sequence, classType):
		query = (" INSERT INTO INFECTED ("
				 " class_type,  ramo_ativ, genero,     vacinado,  sin_dor, dt_dor,  sin_hemo, dt_hemo,"
				 " sin_faget,   dt_faget,  sin_anuria, dt_anuria, sin_adv, exa_tgo, exa_tgp,  exa_bil, "
				 " class_final, evol_caso, est_final,  uf_prob)"
				 " VALUES "
				 " (%s")
		for i in range(0,19): query+=",%s"

		query+=")"

		try:
			self.cursor.execute(query, infected)
			print('\rInfected {} of class {} successfully created!'.format(sequence+1, classType), end="", flush=True)
		except Exception as e:
			print(str(e))

	def generateInfected(self, classType, noisePerc, quantity):
		# classType - Must be in [1,4]
		#	references the infected state:
		#	1 - Light | 2 - Medium | 3 - Severe | 4 - Malignant

		infecPattern = self.getPattern(classType)

		for i in range(quantity):
			newInfected = [infecPattern[0]]
			a = 0 # Remover no código final
			for j in range(1,len(infecPattern)):
				deviation = noisePerc # * self.iszero(infecPattern[j], 1)
				newInfected.append(self.tooBig(self.tooSmall(normal(infecPattern[j], deviation))))
			self.insert(tuple(newInfected), i, classType)

	# o dado vindo do select será o centro do numpy.random.normal
	# já o parâmetro noisePerc será o 'scale' --> Desvio Padrão

	def getInfectedList(self):
		query = ("SELECT ramo_ativ,   genero,      vacinado,  sin_dor,  "
				 " 		 dt_dor,  	  sin_hemo,    dt_hemo,   sin_faget, dt_faget, "
				 " 		 sin_anuria,  dt_anuria,   sin_adv,   exa_tgo, 	 exa_tgp,  "
				 "		 exa_bil, 	  class_final, evol_caso, est_final, uf_prob   "
				 "FROM 	INFECTED")

		try:
			self.cursor.execute(query)
			result = self.cursor.fetchall()
		except Exception as e:
			print(str(e))
			result = [[]]
		return result

	def getPatterns(self):
		query = ("SELECT id_infec,    ramo_ativ,   genero,    vacinado,  sin_dor,  "
				 " 		 dt_dor,  	  sin_hemo,    dt_hemo,   sin_faget, dt_faget, "
				 " 		 sin_anuria,  dt_anuria,   sin_adv,   exa_tgo, 	 exa_tgp,  "
				 "		 exa_bil, 	  class_final, evol_caso, est_final, uf_prob   "
				 "FROM 	INFEC_TYPE")

		try:
			self.cursor.execute(query)
		except Exception as e:
			print(str(e))

		return self.cursor.fetchall()

	def clearDatabase(self):
		query = "DELETE FROM INFECTED"
		try:
			self.cursor.execute(query)
			print("***Database cleared!***")
		except Exception as e:
			print(str(e))

		reset_index = "ALTER TABLE INFECTED AUTO_INCREMENT = 1"

		try:
			self.cursor.execute(reset_index)
			print("***Auto Increment Index Set To 1***")
		except Exception as e:
			print(str(e))

	def getClassType(self):
		query = "SELECT class_type FROM INFECTED"
		try:
			self.cursor.execute(query)
		except Exception as e:
			print(str(e))
		result = self.cursor.fetchall()
		result_f = []
		for i in range(len(result)):
			result_f.append(result[i][0])
		return asarray(result_f)

	def generateDatabase(self, noisePerc, quantity):
		for i in range(1,6):
			self.generateInfected(i, noisePerc, quantity)
			print()
		print("***Database populated!***")

	def endConnection(self):
		self.cursor.close()
		self.cnx.close()