#!/usr/bin/env python
# coding: utf-8

# In[5]:


# # pip install mysql-connector-python
# pip install jupyter
# jupyter notebook 


# In[6]:


import mysql.connector
import pandas as pd 


# In[7]:


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


# In[27]:


url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

dfok=pd.DataFrame()
dfok.columns = [c.replace(' ', '_') for c in dfok.columns]
dfok.columns = [c.replace('/', '_') for c in dfok.columns]

dfok['Carimbo_de_data_hora']=''
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


# In[28]:


print(dfok)


# In[29]:


len(dfok)


# In[30]:


print(dfok[0:5])

dfok2 = dfok[0:1]
print(dfok2)


# In[32]:


values = []
for index,row in dfok2.iterrows():
    CARIMBO = row.Carimbo_de_data_hora
    IDRESPOSTA = row.Questionid
    PERGUNTA = row.Question
    RESPOSTA = row.Answer
    values.append((CARIMBO,ID_RESPOSTA,PERGUNTA,RESPOSTA))
        
insert_values = "".join(str(values).strip('[]'))
sql=(f"INSERT INTO PERGUNTAS_TESTE (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

print(insert_values)
# .
cur.execute(sql)
cnx.commit()


# In[ ]:




