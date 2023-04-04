import pandas as pd
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace = True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']: #['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
        df[columna] = df[columna].apply(lambda x: x.lower())

    for character in ['_', '-']:
        for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
            df[columna] = df[columna].apply(lambda x: x.replace(character, ' '))

    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: re.sub("\$[\s*]", "", x))
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: re.sub(",", "", x))
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: re.sub("\.00", "", x))
    df['monto_del_credito'] = df['monto_del_credito'].apply(int)
    
    df['comuna_ciudadano'] = df['comuna_ciudadano'].apply(float)

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    df.dropna(axis=0,inplace=True)
    # # Se eliminan los registros duplicados
    df.drop_duplicates(inplace = True)

    return df