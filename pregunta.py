import re
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    df.dropna(axis=0, inplace=True)

    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

    for filas in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[filas] = df[filas].str.lower()
        df[filas] = df[filas].str.replace('_', ' ')
        df[filas] = df[filas].str.replace('-', ' ')

    df.drop_duplicates(inplace=True)

    return df

if __name__ == "__main__":
    df = clean_data()
    print(df.dtypes)
    print(df.sexo.value_counts())