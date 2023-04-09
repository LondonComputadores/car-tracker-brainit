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