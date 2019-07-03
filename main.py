import crud
import geoapi
import glob
import pandas as pd
import ddl

#criação das estruturas de dados colocar usuário,senha e host
db = ddl.createStructure("colocar usuario aqui","colocar senha aqui","localhost")

lat = ''
lon = ''

#alimentando a base de dados
for fl in glob.glob('*.txt'):
    f = open(fl, "r") 
    lis = f.readlines()
    for x in lis:
        if  'Lat' in x:
            lat = x.split()[2]
        elif 'Lon' in x:
            lon = x.split()[2]
            feed = geoapi.takeformatedValues(lat,lon)            
            if feed == '':
                continue
            crud.insertValue(db,
                    'locations',
                    "latitude,longitude,rua,numero,bairro,cidade,estado,cep,pais",
                    "{},{},{}".format(lat,lon,feed))
 
#display dos dados usando um dataframe do pandas
df = pd.read_sql('SELECT * FROM locations', con = db)

print(df)