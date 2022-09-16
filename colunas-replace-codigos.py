#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd

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
inicio=(8*216)
fim=(inicio+10)
dfok1 = dfok[inicio:fim]


# In[39]:


display(dfok1)


# In[40]:


lista=[1,2,3,4,5,6,7,8,9,10]
dfok1.insert(1,'AnswerNum2',lista)


# In[41]:


display(dfok1)


# In[42]:


dfok1b=pd.DataFrame()


# In[ ]:


class TrocaWordId(QuestionID,Word):
    
    dict = Dict(
        'question_id' : 1
        'empresas' : {
            'Empresa 1': 'Senior Sistemas',
            'Empresa 2': 'Philips',
            'Empresa 3': 'Ailos',
            'Empresa 4': 'Capgemini',
            'Empresa 5': 'Ambev Tech',
            'Empresa 6': 'Warren',
            'Empresa 7': 'DataInfo',
            'Empresa 8': 'Farmácias App',
            'Empresa 9': 'Havan Labs',
            'Empresa 10': 'T-Systems',
            'Empresa 11': 'Unifique',
        }
        )
    
    def __init__(self,QuestionID,Word):
        self.questionid_from = QuestionID
        self.word_from = Word
        
    def crialista(self):
        
        


# In[45]:


crb=[]
qst=[]
qid=[]
ans=[]




for index,row in dfok1.iterrows():            
    for x in (list(str.split(row.Answer,sep=','))): 
        crb.append(row.Carimbo_de_data_hora)
        qst.append(row.Question)
        qid.append(row.Questionid)
        ans.append(x)
        

dfok1b['Carimbo_de_data_hora'] = crb
dfok1b['Question'] = qst
dfok1b['Questionid'] = qid
dfok1b['Answer'] = ans

    
        


# In[46]:


dfok1b.shape


# In[47]:


display (dfok1b)


# In[ ]:




