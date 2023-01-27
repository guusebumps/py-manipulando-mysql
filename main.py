import mysql.connector

nome_tabela = "NOME DA SUA TABELA"

banco = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="", 
    database="SUADATABASE"
    )

cursor = banco.cursor()
cursor.execute("CREATE TABLE if not exists {} (id INT NOT NULL AUTO_INCREMENT,  exemplo VARCHAR(45) NOT NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;".format(nome_tabela))
banco.commit()
banco.close()   

def inserir():

    valor_inserir = "VALOR QUE DESEJA INSERIR"

    banco = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="SUADATABASE"
        )

    cursor = banco.cursor()
    comando_SQL = ("INSERT INTO {} (exemplo) VALUES (%s)".format(nome_tabela))
    dados = (str(valor_inserir))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    banco.close()

def select():

    banco = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="SUADATABASE"
        )

    cursor = banco.cursor()
    cursor.execute("SELECT * FROM {}".format(nome_tabela))
    dados_lidos = cursor.fetchall()
    banco.commit()
    banco.close() 

    print(dados_lidos)

def delete():

    banco = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="SUADATABASE"
        )

    cursor = banco.cursor()
    cursor.execute("DELETE FROM {} id = VALOR_DO_ID;".format(nome_tabela))
    dados_excluidos = cursor.fetchall()
    banco.commit()
    banco.close() 

    print(dados_excluidos)

def atualizar_tabela():

    banco = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="SUADATABASE"
        )
        
    cursor = banco.cursor()
    cursor.execute("UPDATE {};".format(nome_tabela))
    banco.commit()
    banco.close() 