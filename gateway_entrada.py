import socket
import json
import mysql.connector
import sched
import time
from db_config import config
#from criar_tabelas import criar_tabelas 
#from gateway_tratamento import monitorar_entrada


# Conexão com o banco de dados
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Função para receber a string e salvar no banco de dados
def receber_string(conn, addr):
    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o endereço e porta para conexão
    host = 'localhost'
    port = 3306

    # Faz a conexão
    s.connect((host, port))

    # Recebe a string
    data = s.recv(1024)
    data = data.decode('utf-8')
    values = data.split(";") 

    # Insere a entrada na tabela ENTRADA
    query = "INSERT INTO ENTRADA (campo1, campo2, campo3, campo4) VALUES (%s, %s, %s, %s)"
    #cursor.execute(query, campos)
    cursor.execute(query, (values[0], values[1], values[2], values[3]))

    # Inserir dados na tabela ENTRADA
    # data_entrada = (f"'{campo1}', '{campo2}', '{campo3}', '{campo4}'")
    # cursor.execute(query, data_entrada)

    # Certifica que os dados foram gravados no banco de dados
    cnx.commit()

    conn.sendall(b"Dados armazenados com sucesso!")

    # Verifica se há um comando pendente na tabela COMANDO
    query = "SELECT campo1, campo2, campo3, campo4 FROM COMANDO"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        comando_pendente = ';'.join(str(x) for x in result)

    # Fecha a conexão com o socket
    s.close()

    # Retorna o comando pendente, se houver
    return comando_pendente

# Função para agendar a execução da função receber_string de 20 em 20 segundos
def agendar():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(20, 1, receber_string, ())
    s.run()

    # Fecha a conexão com o banco de dados
    cursor.close()
    cnx.close()

    s.bind(('localhost', 3306))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        receber_string(conn, addr)
        # Executa a função agendar
        agendar()
        time.sleep(20)
#    monitorar_entrada()

print('Gateway executado.')