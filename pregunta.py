import re
import pandas as pd

def clean_data():

    datafrem = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    datafrem.dropna(axis=0, inplace=True)
asd
    datafrem.monto_del_credito = datafrem.monto_del_credito.str.strip("$")
    datafrem.monto_del_credito = datafrem.monto_del_credito.str.replace(",","")
    datafrem.monto_del_credito = datafrem.monto_del_credito.astype(float)
    datafrem.monto_del_credito = datafrem.monto_del_credito.astype(int)

    datafrem.fecha_de_beneficio = pd.to_datetime(datafrem.fecha_de_beneficio, dayfirst=True)

    for filas in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        datafrem[filas] = datafrem[filas].str.lower()
        datafrem[filas] = datafrem[filas].str.replace('_', ' ')
        datafrem[filas] = datafrem[filas].str.replace('-', ' ')

    datafrem.drop_duplicates(inplace=True)

    return datafrem

if __name__ == "__main__":
    datafrem = clean_data()
    print(datafrem.dtypes)
    print(datafrem.sexo.value_counts())