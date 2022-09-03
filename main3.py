import pandas as pd 

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
    df['Questionid']=i    
    df = df.rename(columns={ pergunta : 'Answer'})
    #display(df)
    dfok = dfok.append(df,True)
    #print(dfok.count)
    #print(df.count)




#df.dtypes
#dfok.dtypes