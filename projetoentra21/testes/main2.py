import pandas as pd 

url_or_file=''

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
    print (dfok)
    
 
    #print (dfok[[ 'Carimbo de data/hora']]) 
    # print (dfok.columns[2])
    # print (dfok.columns[3])
    # #display(pd.concat([dfok, df],ignore_index = True))
   

    
    # concatenating
    #display('After concatenating:')
    #display(pd.concat([df1, df2],ignore_index = True))

    # Anterior
    #dfok = dfok.append(df,True)
    #dfok = dfok.concat(df,True)
    




#df.dtypes
#dfok.dtypes
