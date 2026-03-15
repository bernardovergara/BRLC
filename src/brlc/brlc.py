import unicodedata
import pandas as pd
from importlib.resources import files

db_path = files("brlc").joinpath("db.xlsx")
df = pd.read_excel(db_path)


def normalize(text):
    return (unicodedata.normalize('NFKD', str(text))
            .encode('ascii', errors='ignore')
            .decode('utf-8')
            .lower()
            .strip())


uf_dict = {
    'AC': 'Acre','AL': 'Alagoas','AP': 'Amapá','AM': 'Amazonas','BA': 'Bahia',
    'CE': 'Ceará','DF': 'Distrito Federal','ES': 'Espírito Santo','GO': 'Goiás',
    'MA': 'Maranhão','MT': 'Mato Grosso','MS': 'Mato Grosso do Sul','MG': 'Minas Gerais',
    'PA': 'Pará','PB': 'Paraíba','PR': 'Paraná','PE': 'Pernambuco','PI': 'Piauí',
    'RJ': 'Rio de Janeiro','RN': 'Rio Grande do Norte','RS': 'Rio Grande do Sul',
    'RO': 'Rondônia','RR': 'Roraima','SC': 'Santa Catarina','SP': 'São Paulo',
    'SE': 'Sergipe','TO': 'Tocantins',
}

# --------- INDEXES ---------

uf_by_id = dict(zip(df["UF"], df["Nome_UF"]))

id_by_uf = {
    normalize(name): uf
    for uf, name in uf_by_id.items()
}

city_by_id = dict(zip(
    df["Código Município Completo"],
    df["Nome_Município"]
))

id_by_city = {
    normalize(name): code
    for code, name in city_by_id.items()
}

# --------- API ---------

def get_uf_by_abbr(abbr: str):
    return uf_dict.get(abbr.upper())


def get_uf_by_id(id: int):
    return uf_by_id.get(id)


def get_id_by_uf(uf: str):
    if len(uf) == 2:
        uf = get_uf_by_abbr(uf)

    return id_by_uf.get(normalize(uf))


def get_city_by_id(id: int):
    return city_by_id.get(id)


def get_id_by_city(city: str):
    return id_by_city.get(normalize(city))