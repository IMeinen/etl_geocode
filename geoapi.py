import urllib.request
import json 

endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" #endereço da api do googlemaps
apikey   = "AIzaSyA3snXifLrkFA2Rmgfqg52Squz3mi2txtg" #chave da minha conta

#validação do formato do CEP
def validateCEP(cep):
    try:
        a,b = map(str,cep.split('-'))
    except ValueError:
        return False    
    if a.strip().isnumeric() and b.strip().isnumeric():
        return True

#recebe como parametro a latitude e a longitude e retorna um dicionário com as informações enriquecidas    
def takeValues(lat,lon):
    navreq = "latlng={},{}&key={}&language=pt-BR&result_type=street_address".format(lat,lon,apikey)
    request = endpoint + navreq
    response = urllib.request.urlopen(request, timeout = 30).read()    
    dic = {}
    try:
        response = json.loads(response)['results'][0]['formatted_address'].split(',')
    except IndexError:
        return ''
    print('LOG - {}'.format(str(response)))
    try:
        dic['endereco'] = response[0].strip(' ')
    except IndexError:
        dic['endereco'] = ''
    try:
        dic['numero']   = response[1].split('-')[0].strip(' ')
    except IndexError:
        dic['numero']   = ''
    try:        
        dic['bairro']   = response[1].split('-')[1].strip(' ')
    except IndexError:
        dic['bairro']   = ''
    try:
        dic['cidade']   = response[2].split('-')[0].strip(' ')
    except IndexError:
        dic['cidade']   = ''
    try:
        dic['estado']   = response[2].split('-')[1].strip(' ')
    except IndexError:
        dic['estado']   = ''
    try:
        if validateCEP(response[3]):                   
            dic['cep']      = response[3].strip(' ')
        else:
            dic['cep']      = ''
    except IndexError:
        dic['cep']      = ''
    try:
        dic['pais']     = response[4].strip(' ')
    except IndexError:
        dic['pais']     = response[3].strip(' ')
  

    return dic

#formata o dicionario de dados retornado pela takeValues e retorna uma string para usar na função de inserção no banco
def takeformatedValues(lat,lon):
    feed = takeValues(lat,lon)
    if feed == '':
        return ''
    feed = [feed[x] for x in feed.keys()]  
    feed = ('","'.join(feed))
    feed = '\"' + feed + '\"'
    return feed


