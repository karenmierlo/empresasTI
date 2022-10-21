import mysql.connector
import pandas as pd 
#


cnx = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
    )

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS PERGUNTAS_TCC; 
""")

cur.execute("""    
    CREATE TABLE PERGUNTAS_TCC(
            PERGUNTAS_CARIMBO TEXT NOT NULL,
            PERGUNTAS_ID_RESPOSTA INTEGER,
            PERGUNTAS_NOME TEXT NOT NULL,
            PERGUNTAS_RESPOSTA TEXT NOT NULL
    );
""")
# df.groupby(['col1', 'col2']).size()
#  Tabela de PERGUNTAS_TCC
url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

dfok=pd.DataFrame()

dfok['Carimbo de data/hora']=''
dfok['Answer']=''
dfok['Question']=''
dfok['Questionid']=''

for i in range(1,14):
    colunas=[0,i]
    df = pd.read_csv(url_or_file, header=0,usecols=colunas)
    pergunta=df.columns[1]
    df['Question']=pergunta
    df['Questionid']=i
    df = df.rename(columns={ pergunta : 'Answer'})    
    dfok = (pd.concat([dfok, df],ignore_index = True))

    #print(dfok.dtypes)

values = []


print(len(dfok))


# for index,row in dfok.iterrows():

#     CARIMBO = dfok[[ 'Carimbo de data/hora']]  
#     IDRESPOSTA = dfok[[ 'Questionid']]  
#     PERGUNTA = dfok[[ 'Answer']]  
#     RESPOSTA = dfok[[ 'Question']]   
#     values.append((CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))
    
        
# insert_values = "".join(str(values).strip('[]'))
# sql=(f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")
# cur.execute(sql)
# cnx.commit()
