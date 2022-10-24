# Bibliotecas Utilizadas
import mysql.connector
import pandas as pd

# - Importando planilha google docs
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrGR2RwQBQAbt3Mzu0UbgKMGSY1hxXtt8rV1fcLzrwjRy2KBDUaSOoT5EKt-j0t6cxZ0KIz-4O0ZVf/pub?gid=891049362&single=true&output=csv'

# Criando Dataframe vazio onde recebera atravez do laço for, 
# todas as perguntas com suas respostas das (14) colunas.

df = pd.DataFrame()
df['Carimbo_de_data_hora'] = ''
df['Answer'] = ''
df['Question'] = ''
df['Questionid'] = ''

# No laço for abaixo percorremos todas as 
# colunas do CSV adicionando dm df_coluna_by_coluna

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

# Abaixo criamos uma codificação para os nomes 
# de empresas e outros detalhes.

def verifica(base8, empresa):
    ret = 'None'
    for a, b in base8.items():
        if (str.strip(a) == str.strip(empresa)):
            ret = b
    return ret

# Aqui criamos um dicionário de dados
# para suprimir/alterar o nome da empresa

base8 = {
    'Empresa1': 'Empresa 1',
    'Empresa2': 'Empresa 2',
    'Empresa3': 'Empresa 3',
    'Empresa4': 'Empresa 4',
    'Empresa5': 'Empresa 5',
    'Empresa6': 'Empresa 6',
    'Empresa7': 'Empresa 7',
    'Empresa8': 'Empresa 8',
    'Empresa9': 'Empresa 9',
    'Empresa10': 'Empresa 10',
    'Empresa11': 'Empresa 11'
}

# dataframe Nova Serialização
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
            ans_code.append(verifica(base8, answerseparada))
        
        else:
            ans_code.append(answerseparada)


dfns['Carimbo_de_data_hora'] = crb
dfns['Question'] = qst
dfns['Questionid'] = qid
dfns['Answer'] = ans
dfns['AnswerCode'] = ans_code
# A linha abaixo é responsável por excluir os espaços em branco após a vírgula nas respostas coletadas.
dfns['AnswerCode'] = dfns['AnswerCode'].str.strip()

# Conexão com o servidor
cnx = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)
cur = cnx.cursor()

# Se existir a tabela, ela será deletada
cur.execute("""
    DROP TABLE IF EXISTS PERGUNTAS_TCC; 
""")

# Criação do Schema da Tabela
cur.execute("""    
    CREATE TABLE PERGUNTAS_TCC(
            PERGUNTAS_CARIMBO DATE NOT NULL,
            PERGUNTAS_ID_RESPOSTA INTEGER,
            PERGUNTAS_NOME TEXT NOT NULL,
            PERGUNTAS_RESPOSTA TEXT NOT NULL
    );
""")

divisoes = int((len(dfns))/1000+1)

contador = 0
print(divisoes)

def insere_valores(inicio, fim):
    contador = 0
    print(inicio, fim)
    
    # Criando uma lista
    values = []
    for index, row in dfns[inicio:fim].iterrows():
        for xresp in (list(str.split(row.AnswerCode, sep=','))):
            CARIMBO = row.Carimbo_de_data_hora
            IDRESPOSTA = row.Questionid
            PERGUNTA = row.Question
            RESPOSTA = xresp
            contador = contador + 1
            values.append((CARIMBO, IDRESPOSTA, PERGUNTA, RESPOSTA))
            
    insert_values = "".join(str(values).strip('[]'))
    # Inserindo os valores
    sql = (f"INSERT INTO PERGUNTAS_TCC (PERGUNTAS_CARIMBO,PERGUNTAS_ID_RESPOSTA,PERGUNTAS_NOME,PERGUNTAS_RESPOSTA) VALUES {insert_values}")

    cur.execute(sql)
    cnx.commit()


divisoes = int((len(dfns))/1000+1)

total = int(len(dfns))
passo = int(len(dfns)/divisoes)
saldo = total

x, inicio, fim = 0, 0, 0
lista = []

while saldo > 0:
    fim = fim+passo
    
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
    insere_valores(x, y)




