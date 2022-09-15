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
    DROP TABLE IF EXISTS PERGUNTAS_TCC; 
""")

cur.execute("""    
    CREATE TABLE PERGUNTAS_TCC(
            PERGUNTAS_CARIMBO DATE NOT NULL,
            PERGUNTAS_ID_RESPOSTA INTEGER,
            PERGUNTAS_NOME TEXT NOT NULL,
            PERGUNTAS_RESPOSTA TEXT NOT NULL
    );
""")



#url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'
url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'
url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

dfok=pd.DataFrame()
dfok.columns = [c.replace(' ', '_') for c in dfok.columns]
dfok.columns = [c.replace('/', '_') for c in dfok.columns]

dfok['Carimbo_de_data_hora']=''
dfok['Answer']=''
dfok['Question']=''
dfok['Questionid']=''

#df['col'] = pd.to_datetime(df['col'])

for i in range(1,14):
    colunas=[0,i]
    df = pd.read_csv(url_or_file, header=0,usecols=colunas)
    pergunta=df.columns[1]    
    df = df.rename(columns={ pergunta : 'Answer'})    
    df['Question']=pergunta
    df['Questionid']=i        
    dfok = (pd.concat([dfok, df],ignore_index = True))
    dfok['Carimbo_de_data_hora']= (pd.to_datetime(dfok['Carimbo_de_data_hora']))
    


#print(dfok)

len(dfok)

#print(dfok[0:1100])

# dfok1 = dfok[0:1085]
dfok1 = dfok[600:1600]
dfok2 = dfok[1086:1999]
dfok3 = dfok[2000:2830]

#print(dfok2)




values = []
for index,row in dfok1.iterrows():    
    for xresp in (list(str.split(row.Answer,sep=','))):
        CARIMBO = row.Carimbo_de_data_hora
        IDRESPOSTA = row.Questionid
        PERGUNTA = row.Question
        RESPOSTA = xresp 
        print (CARIMBO,IDRESPOSTA,PERGUNTA,xresp)
        values.append((CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))
        
        
insert_values = "".join(str(values).strip('[]'))
sql=(f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

#print(insert_values)
cur.execute(sql)
cnx.commit()

# values = []
# for index,row in dfok2.iterrows():
#     CARIMBO = row.Carimbo_de_data_hora
#     IDRESPOSTA = row.Questionid
#     PERGUNTA = row.Question
#     RESPOSTA = row.Answer
#     values.append((CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))
        
# insert_values = "".join(str(values).strip('[]'))
# sql=(f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

# #print(insert_values)
# cur.execute(sql)
# cnx.commit()

# values = []
# for index,row in dfok3.iterrows():
#     CARIMBO = row.Carimbo_de_data_hora
#     IDRESPOSTA = row.Questionid
#     PERGUNTA = row.Question
#     RESPOSTA = row.Answer
#     values.append((CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))
        
# insert_values = "".join(str(values).strip('[]'))
# sql=(f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

# #print(insert_values)
# cur.execute(sql)
# cnx.commit()
