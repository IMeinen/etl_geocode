import mysql.connector

#Conexao com o banco de dados | parametros(host,usuario,senha,base de dados(se houver))
def conectBanco(mhost,muser,mpassword,mdbase = ''):
  db = mysql.connector.connect(
    host     = mhost,     #EX: "localhost"     
    user     = muser,     #EX: root"
    passwd   = mpassword, #EX: "9qljf{)k$Zh:"
    database = mdbase     #EX: "minhadatabase"
   ) 
  return db

#Criação da base de dados | parametros(conector,nome da base de dados)
def createDatabase(mdb,mnome):
  mycursor = mdb.cursor()
  mycursor.execute("CREATE DATABASE {}".format(mnome))

#Criação de tabelas | parametros(conector,nome da tabela,campos e tipos em formato str)
def createTable(mdb,nome,values):
  mycursor = mdb.cursor()    
  mycursor.execute("CREATE TABLE {} ({})".format(nome,values))

#Inserção de registro em uma tabela | parametros(conector,nome da tabela,campos,valores)
def insertValue(mdb,mtable,mfields,mvalues):
  mycursor = mdb.cursor()
  query  = "INSERT INTO {} ({}) VALUES ({})".format(mtable,mfields,mvalues)   
  mycursor.execute(query)
  mdb.commit()

#Seleção de um registro na tabela | parametros(conector,nome da tabela,campos , query de filtro)
def selectValue(mdb,mtable,mfields = '*',mquery = ''):
  mycursor = mdb.cursor()
  query  = "SELECT {} FROM {}{}".format(mfields,mtable,mquery)   
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  return myresult

#Atualização de um registro na tabela | parametros(conector,nome da tabela,alteração(ex: nome = joão) , query de filtro)
def updateValue(mdb,mtable,mchange,mclause):
  mycursor = mdb.cursor()  
  query = "UPDATE {} SET {} WHERE {}".format(mtable,mchange,mclause)
  mycursor.execute(query)
  mdb.commit()

#Exclusão de um registro na tabela | parametros(conector,nome da tabela, query de filtro)
def deleteValue(mdb,mtable,mclause):
  mycursor = mdb.cursor()  
  query    = "DELETE FROM {} WHERE {}".format(mtable,mclause)
  mycursor.execute(query)
  mdb.commit()
