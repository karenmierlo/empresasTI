import pandas as pd 
#

url_or_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

dfok=pd.DataFrame()

dfok['Carimbo de data/hora']=''
dfok['Answer']=''
dfok['Question']=''
dfok['Questionid']=''
dfok['id']=''


for i in range(1,14):
    colunas=[0,i]
    df = pd.read_csv(url_or_file, header=0,usecols=colunas)
    pergunta=df.columns[1]
    df['Question']=pergunta
    df = df.rename(columns={ pergunta : 'Answer'})
    
    valor=[]
    for i in range(len(dfok),len(df)+len(dfok)):
        valor.append(i)
    df.insert(5, 'id', valor)                            
    df.set_index('id')
    dfok = dfok.concat([dfok,df])
    
    

## a coluna ID do dfok deve receber '' (ok)
## a coluna ID do df deve receber um range de lenght de dfok + 1 ao lenght dela. 
## usar o comando df.insert(conforme exemplo em teste.ipynb)
## df.set_index(xxxx) para modificar o index das duas tabelas. 
## depois fazer o df.concat([dfok,df],outer) e informar que a coluna index é a id em ambas. 
## não permitir que o concat utilize a coluna carimbo de data/hora para merge ou concat 




#df.dtypes
#dfok.dtypes
