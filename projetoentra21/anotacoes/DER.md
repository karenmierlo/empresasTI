Cursos
-
curso_iD PK int
curso_nome string

Modalidade
-
modalidade_iD PK int
modalidade_nome string

Periodo
-
periodo_iD PK int
periodo_nome string

Faixa_Etaria
-
faixa_etaria_iD PK int
faixa_etaria_intervalo string

Genero
-
genero_iD PK int
formato_nome string

Empresas
-
empresa_iD PK int
empresa_nome string
empresa_seguimento string
empresa_beneficio_ID int FK >- Beneficios.Beneficio_ID

Interesse
-
interesse_iD PK int
interesse_tipo string

Beneficios
-
beneficio_iD PK int
beneficio_nome string


Modalidade_Emprego
----
modalidade_iD PK int
modalidade_nome string

Tipo_Vaga 
------------
tipo_vaga_iD PK int
tipo_vaga_Nome  string

Idiomas
----
idioma_iD PK int
idioma_nome string

Fluencia
----
fluencia_iD PK int
fluencia_nome string

