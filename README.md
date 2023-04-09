Passo a passo para a solução do proplema proposto:

1. Database:

    ToDo:

    - 1. Criar a tabela Entrada (Armazenará a string recebida)
    - 2. Salvar a string no formato col. ou "campo1; campo2; campo3; campo4".
    - 3. Criar a tabela Tratamento (Armazenar a string após formatada)
    - 4. Formatar e armazenar a string da tabela de Entrada em seus devidos campos após ser sub-dividida.
    - 5. Criar a tabela Comando (Receberá os comandos pendentes)
    - 6. Ao receber a string da tabela Entrada, verificar essa tabela e retornar a string nessa mesma tabela e fazer o que? Onde? Como? Para que?

    Requirements:

    - 1. Uma "String"
    - 2. Quatro campos para receber essa string sub-dividida em 4 

    Parameters:

    Tabelas:
    - 1. :param campo1: string
    - 2. :param campo2: string
    - 3. :param campo3: string
    - 4. :param campo4: string

2. Gateway Entrada:

    ToDo:

    - 1. Deve ficar esperando receber a string (separado por “;”)
    - 2. Retornar a string salva na tabela de comando_pendente

        extra mile:

        - 1. Implementar via socket
        - 2. Agendar intervalos de 20s entre as execuções da tarefa

    Requirements:

    - 1. string_received
    - 2. string_formatted
    - 3. retorno 

    Parameters:

    - 1. :param string_received: str
    - 2. :param string_formatted: str
    - 3. :param return string_formatted: str or collection

3. Gateway Tratamento:

    ToDo:

    - 1. Deve monitorar a tabela criada com a string recebida e salvar cada posição da string em um campo da tabela

        extra mile:

        - 1. Agendar intervalos de 20s entre as execuções da tarefa 

    Requirements:

    - 1. ? 

    Parameters:

    - 1. ?

4. Dockers:

    ToDo:

    - 1. 

    Requirements:

    - 1.  

    Parameters:

    - 1.  

    ----------------------------------------------------------


    References:

    1. https://www.mysqltutorial.org/mysql-application-programming-interfaces/
    2. https://www.mysqltutorial.org/getting-started-with-mysql/connect-to-mysql-server/
    3. https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
    4. https://dev.mysql.com/doc/connector-python/en/onnector-python-example-cursor-transaction.html
    5. https://dev.mysql.com/doc/refman/8.0/en/spatial-types.html
    6. https://mothishdeenadayalan.medium.com/containerizing-a-python-app-mysql-python-docker-1ce64e444ed9
    7. https://hub.docker.com/_/mysql
    8. https://docs.python.org/3/library/socket.html
    9. https://docs.python.org/3/library/sched.html
    10. https://docs.python.org/3/library/socketserver.html
    11. https://books.goalkicker.com/PythonBook/
    12. https://realpython.com/python-sockets/
    13. https://realpython.com/async-io-python/
    14. https://realpython.com/location-based-app-with-geodjango-tutorial/
    15. https://www.tornadoweb.org/en/stable/