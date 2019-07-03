import crud

#criação das estruturas de dados
def createStructure(user,password,host = 'localhost'):
    db = crud.conectBanco(host,user,password)
    crud.createDatabase(db,"locations_database")
    db = crud.conectBanco(host,user,password,"locations_database")
    crud.createTable(db,
                 "locations",
                 "id INT AUTO_INCREMENT PRIMARY KEY, latitude VARCHAR(255), longitude VARCHAR(255), rua VARCHAR(255),numero VARCHAR(255),bairro VARCHAR(255),cidade VARCHAR(255),cep VARCHAR(255),estado VARCHAR(255),pais VARCHAR(255)")

    return db