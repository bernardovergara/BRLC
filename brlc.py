import unicodedata
import pandas as pd

df = pd.read_excel('test/db.xlsx')

uf_dict = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins',
}

def normalize(text):
    return (unicodedata.normalize('NFKD', text)
            .encode('ascii', errors='ignore')
            .decode('utf-8')
            .lower()
            .strip())

def get_uf_by_abbr(abbr: str):
    abbr.upper()
    if abbr in uf_dict.keys():
        return uf_dict[abbr]

def get_uf_by_id(id: int):
    return df[df['UF'] == id]['Nome_UF'].values[0]

def get_id_by_uf(uf: str):
    if len(uf) == 2:
        uf = get_uf_by_abbr(uf)
        
    uf = normalize(uf)
    return df[df['Nome_UF'].apply(normalize) == uf]['UF'].values[0]

def get_city_by_id(id: int):
    return df[df['Código Município Completo'] == id]['Nome_Município'].values[0]

def get_id_by_city(city: str):
    city = normalize(city)
    return df[df['Nome_Município'].apply(normalize) == city]['Código Município Completo'].values[0]