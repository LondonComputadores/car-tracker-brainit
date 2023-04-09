import mysql.connector
import time
from db_config import config


# Conexão com o banco de dados
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Função para monitorar a tabela ENTRADA e salvar cada posição em um campo da tabela TRATAMENTO
def monitorar_entrada():
    # Consulta as entradas não processadas na tabela ENTRADA
    query = "SELECT campo1, campo2, campo3, campo4 FROM ENTRADA"
    cursor.execute(query)
    entradas = cursor.fetchall()

    # Processa cada entrada
    for entrada in entradas:
        # Salva cada posição em um campo da tabela TRATAMENTO
        query = "INSERT INTO TRATAMENTO (campo1, campo2, campo3, campo4) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, entrada)
        cnx.commit()

# Executa a função monitorar_entrada a cada 20 segundos
while True:
    monitorar_entrada()
    time.sleep(20)
    print('Tratamento executado.')