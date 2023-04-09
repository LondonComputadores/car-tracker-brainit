import mysql.connector
from db_config import config
#from gateway_entrada import receber_string
#from gateway_tratamento import monitorar_entrada


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def criar_tabelas():

    # Cria tabela ENTRADA
    query = "CREATE TABLE IF NOT EXISTS ENTRADA (id INT AUTO_INCREMENT PRIMARY KEY, campo1 VARCHAR(255), campo2 VARCHAR(255), campo3 VARCHAR(255), campo4 VARCHAR(255))"
    cursor.execute(query)

    # Cria tabela TRATAMENTO
    query = "CREATE TABLE IF NOT EXISTS TRATAMENTO (id INT AUTO_INCREMENT PRIMARY KEY, campo1 VARCHAR(255), campo2 VARCHAR(255), campo3 VARCHAR(255), campo4 VARCHAR(255))"
    cursor.execute(query)

    # Cria tabela COMANDO
    query = "CREATE TABLE IF NOT EXISTS COMANDO (id INT AUTO_INCREMENT PRIMARY KEY, campo1 VARCHAR(255), campo2 VARCHAR(255), campo3 VARCHAR(255), campo4 VARCHAR(255))"
    cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    criar_tabelas()
    
#print('Tabelas executado')