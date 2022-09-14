import mysql.connector
import pandas as pd 



cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g3',
    password = 'e2122g3@16@ago',
    database = 'e2122g3'
    )

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS PERGUNTAS_TESTE; 
""")

cur.execute("""    
    CREATE TABLE PERGUNTAS_TESTE(
            PERGUNTAS_CARIMBO TEXT NOT NULL,
            PERGUNTAS_ID_RESPOSTA INTEGER,
            PERGUNTAS_NOME TEXT NOT NULL,
            PERGUNTAS_RESPOSTA TEXT NOT NULL
    );
""")
# df.groupby(['col1', 'col2']).size()
#  Tabela de PERGUNTAS_TESTE
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=1689922439&single=true&output=csv'
colunas = list(['CARIMBO','IDRESPOSTA','PERGUNTA','RESPOSTA'])

df = pd.read_csv(url_or_file)

values = []
for index,row in df.iterrows():
    CARIMBO = row.CARIMBO
    IDRESPOSTA = row.IDRESPOSTA
    PERGUNTA = row.PERGUNTA
    RESPOSTA = row.RESPOSTA
    values.append((CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))
        
insert_values = "".join(str(values).strip('[]'))
sql=(f"INSERT INTO PERGUNTAS_TESTE (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

print(insert_values)
# .
cur.execute(sql)
cnx.commit()
