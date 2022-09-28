import mysql.connector
import pandas as pd


def pp(a):
    print('a', end='')


#url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

df = pd.DataFrame()
df['Carimbo_de_data_hora'] = ''
df['Answer'] = ''
df['Question'] = ''
df['Questionid'] = ''


for i in range(1, 14):
    colunas = [0, i]
    df_coluna_by_coluna = pd.read_csv(url_or_file, header=0, usecols=colunas)
    pergunta = df_coluna_by_coluna.columns[1]
    df_coluna_by_coluna = df_coluna_by_coluna.rename(
        columns={pergunta: 'Answer'})
    df_coluna_by_coluna['Question'] = pergunta
    df_coluna_by_coluna['Questionid'] = i

    df = (pd.concat([df, df_coluna_by_coluna], ignore_index=True))
    df['Carimbo_de_data_hora'] = (pd.to_datetime(df['Carimbo_de_data_hora']))
    df['Questionid'] = (pd.to_numeric(df['Questionid']))

print(len(df))

pp('b1')
# teste 

def verifica(base8, empresa):
    pp('b2')
    ret = 'None'
    for a, b in base8.items():
        if (str.strip(a) == str.strip(empresa)):
            ret = b
    print(f'verifica() --> Base:{empresa}:,:{ret}:')
    return ret


pp('b3')


base8 = {
    'Senior Sistemas': 'Empresa1',
    'Philips': 'Empresa2',
    'Ailos': 'Empresa3',
    'Capgemini': 'Empresa4',
    'Ambev Tech': 'Empresa5',
    'Warren': 'Empresa6',
    'DataInfo': 'Empresa7',
    'Farmácias App': 'Empresa8',
    'Havan Labs': 'Empresa9',
    'T-Systems': 'Empresa10',
    'Unifique': 'Empresa11'
}


pp('b4')


# dataframe New Serializer
dfns = pd.DataFrame()

crb = []
qst = []
qid = []
ans = []
ans_code = []

for index, row in df.iterrows():
    for answerseparada in (list(str.split(row.Answer, sep=','))):        
        crb.append(row.Carimbo_de_data_hora)
        qst.append(row.Question)
        qid.append(row.Questionid)
        ans.append(answerseparada)
        if (row.Questionid == 8):
            print(f'AnswerSeparada:{answerseparada}:')
            ans_code.append(verifica(base8, answerseparada))
        # elif (row.Questionid == 9):
        #     ans_code.append(verifica(base9, answerseparada))
        else:
            ans_code.append(answerseparada)


dfns['Carimbo_de_data_hora'] = crb
dfns['Question'] = qst
dfns['Questionid'] = qid
dfns['Answer'] = ans
dfns['AnswerCode'] = ans_code


print(dfns.shape)


print("aqui")
print(dfns)
print("ok")

pp('mysql')
cnx = mysql.connector.connect(
    host='3.89.36.150',
    user='e2122g3',
    password='e2122g3@16@ago',
    database='e2122g3'
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
pp('mysql create database')


divisoes = int((len(dfns))/1000+1)

contador = 0
print(divisoes)


def insere_valores(inicio, fim):
    contador = 0
    print(inicio, fim)
    values = []
    for index, row in dfns[inicio:fim].iterrows():
        for xresp in (list(str.split(row.AnswerCode, sep=','))):
            pp('F')
            CARIMBO = row.Carimbo_de_data_hora
            IDRESPOSTA = row.Questionid
            PERGUNTA = row.Question
            RESPOSTA = xresp
            contador = contador + 1
            values.append((CARIMBO, IDRESPOSTA, PERGUNTA, RESPOSTA))
            # print((inicio,fim,CARIMBO,IDRESPOSTA,PERGUNTA,RESPOSTA))

    insert_values = "".join(str(values).strip('[]'))
    sql = (
        f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

    print(f'Contador: {contador}')

    cur.execute(sql)
    cnx.commit()


divisoes = int((len(dfns))/1000+1)

print(divisoes)

total = int(len(dfns))
passo = int(len(dfns)/divisoes)
saldo = total

x, inicio, fim = 0, 0, 0
lista = []

while saldo > 0:
    pp('G')
    fim = fim+passo
    print(f'saldo: {saldo} passo: {passo}')

    if saldo < passo:
        fim = inicio + (saldo-1)
    else:
        fim = inicio + (passo - 1)

    saldo = saldo-passo
    if saldo < 10:
        fim = fim + saldo
        saldo = saldo - saldo
    lista.append((inicio, fim))

    # inicio = inicio + passo +1
    inicio = fim + 1

for x, y in lista:
    print(f'*************: {x},{y} = {y-x}')
    insere_valores(x, y)


cnx = mysql.connector.connect(
    host='3.89.36.150',
    user='e2122g3',
    password='e2122g3@16@ago',
    database='e2122g3'
)
cur = cnx.cursor()
pp('H')
cur.execute("""
    SELECT COUNT(*) FROM PERGUNTAS_TCC; 
""")

pp('I')

print(f'Contador Mysql: {cur.fetchone()} ')