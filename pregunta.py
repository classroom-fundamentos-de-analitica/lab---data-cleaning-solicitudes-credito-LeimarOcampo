import pandas as pd
import re
from datetime import datetime

def clean_data():

    datafrem = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    datafrem.dropna(axis=0,inplace=True)
    datafrem.drop_duplicates(inplace = True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']: #['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
        datafrem[columna] = datafrem[columna].apply(lambda x: x.lower())

    for character in ['_', '-']:
        for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
            datafrem[columna] = datafrem[columna].apply(lambda x: x.replace(character, ' '))

    datafrem['monto_del_credito'] = datafrem['monto_del_credito'].apply(lambda x: re.sub("\$[\s*]", "", x))
    datafrem['monto_del_credito'] = datafrem['monto_del_credito'].apply(lambda x: re.sub(",", "", x))
    datafrem['monto_del_credito'] = datafrem['monto_del_credito'].apply(lambda x: re.sub("\.00", "", x))
    datafrem['monto_del_credito'] = datafrem['monto_del_credito'].apply(int)
    
    datafrem['comuna_ciudadano'] = datafrem['comuna_ciudadano'].apply(float)

    datafrem['fecha_de_beneficio'] = datafrem['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    datafrem.dropna(axis=0,inplace=True)
    # # Se eliminan los registros duplicados
    datafrem.drop_duplicates(inplace = True)

    return datafrem