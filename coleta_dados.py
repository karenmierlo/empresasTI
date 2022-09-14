import mysql.connector
import pandas as pd 
#import random


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g3',
    password = 'e2122g3@16@ago',
    database = 'e2122g3'
    )

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS EMPRESA_G3_V2; 
""")

cur.execute("""    
    CREATE TABLE EMPRESA_G3_V2(
            EMPRESA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            EMPRESA_NOME TEXT NOT NULL,
            EMPRESA_TIPO TEXT NOT NULL,
            EMPRESA_PONTUACAO INTEGER NOT NULL
    );
""")
# df.groupby(['col1', 'col2']).size()
#  Tabela de Empresa_G3_V2
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTThFyCgEMcqO55iNcgqoiGTf4f4oYi82xwghHLa4unT3ftUhJ0EguCe9RyrD8EijJI9sHxMR8uxnto/pub?gid=455532436&single=true&output=csv'
colunas = list(['ID','EMPRESA','BENEFICIO','PONTUACAO'])

df = pd.read_csv(url_or_file)

values = []
for index,row in df.iterrows():
    NOME = row.EMPRESA
    TIPO = row.BENEFICIO
    PONTUACAO = row.PONTUACAO
    values.append((NOME,TIPO,PONTUACAO))
        
insert_values = "".join(str(values).strip('[]'))
sql=(f"INSERT INTO EMPRESA_G3_V2 (EMPRESA_NOME,EMPRESA_TIPO,EMPRESA_PONTUACAO) VALUES {insert_values}")

# print(insert_values)
cur.execute(sql)
cnx.commit()    
