# Bibliotecas Utilizadas
import mysql.connector
import pandas as pd 


# Conexão com o servidor
cnx = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
    )

cur = cnx.cursor()

# Se a tabela já existir, será deletada
cur.execute("""
    DROP TABLE IF EXISTS EMPRESA_G3_V2; 
""")

# Criação do Schema da tabela
cur.execute("""    
    CREATE TABLE EMPRESA_G3_V2(
            EMPRESA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            EMPRESA_NOME TEXT NOT NULL,
            EMPRESA_TIPO TEXT NOT NULL,
            EMPRESA_PONTUACAO INTEGER NOT NULL
    );
""")
# - Importando planilha google docs
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTThFyCgEMcqO55iNcgqoiGTf4f4oYi82xwghHLa4unT3ftUhJ0EguCe9RyrD8EijJI9sHxMR8uxnto/pub?gid=455532436&single=true&output=csv'
colunas = list(['ID','EMPRESA','BENEFICIO','PONTUACAO'])

# Criando Dataframe vazio onde recebera atravez do laço for, 
# todos os beneficios das empresas pesquisadas.

df = pd.read_csv(url_or_file)

values = []
for index,row in df.iterrows():
    NOME = row.EMPRESA
    TIPO = row.BENEFICIO
    PONTUACAO = row.PONTUACAO
    values.append((NOME,TIPO,PONTUACAO))
        
insert_values = "".join(str(values).strip('[]'))
# Inserindo os dados na tabela
sql=(f"INSERT INTO EMPRESA_G3_V2 (EMPRESA_NOME,EMPRESA_TIPO,EMPRESA_PONTUACAO) VALUES {insert_values}")

# print(insert_values)
cur.execute(sql)
cnx.commit()    
