# %%
import pandas as pd 



# %% [markdown]
# Para inicializar este código utilize o comando: pip install -U ipykernel 
# ou faça pip freeze -r requirements.txt dentro do venv local de cada usuario. 

# %% [markdown]
# Vamos criar um dataframe que recebera por append todas as informações das colunas especificas (são 14 ao total, são as perguntas).
# O titulo de cada coluna sera transportado pelo DataFrame.colunas[0]
# 
# cada append será feito com uma query do pandas por coluna. 

# %%
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
    #display(df)
    dfok = dfok.append(df,True)
    #print(dfok.count)
    #print(df.count)




#df.dtypes
#dfok.dtypes

    


# %%
pd.set_option('display.max_rows', None)

display(dfok)
display(dfok)




