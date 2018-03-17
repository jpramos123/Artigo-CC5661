import mysql.connector as con

cnx = con.connect(	user='mvp', 
					password='epidemiologia',
    	        	host='johnny.heliohost.org',
        	    	database='mvp_viral')
        	    	
cursor = cnx.cursor()

def end():
	cursor.close()
	cnx.close()
	
def query():
	query = ("SELECT uf_infec,	 dt_infec,  ramo_ativ,   genero," 
			 "		 vacinado,   sin_faget, dt_faget,    sin_dor,"
			 "		 sin_anuria, sin_hemo,  dt_dor,      dt_anuria,"
			 "		 dt_hemo,    sin_adv,	desc_sinadv, exa_tgo,"
			 "		 exa_tgp,	 exa_bil,   class_final, evol_caso," 
			 "		 est_final,  dt_enc, '' as 'seed'"
			 "FROM 	INFECTADOS")

	cursor.execute(query)
	rows = cursor.fetchall()
	end()
	return rows

