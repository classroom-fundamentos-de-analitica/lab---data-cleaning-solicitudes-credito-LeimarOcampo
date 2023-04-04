import pandas as pd
def clean_data():

    datafrem = pd.read_csv("solicitudes_credito.csv", sep=";")
    datafrem.dropna(axis = 0, inplace = True)
    datafrem.drop_duplicates(inplace = True)
    datafrem=datafrem.drop(['Unnamed: 0'], axis=1)
    datafrem[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]]=datafrem[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    datafrem=datafrem.replace(to_replace="(_)|(-)",value=" ",regex=True)    
    datafrem=datafrem.replace(to_replace="[,$]|(\.00$)",value="",regex=True)
    datafrem.monto_del_credito = datafrem.monto_del_credito.astype("int")
    datafrem.comuna_ciudadano = datafrem.comuna_ciudadano.astype("float")
    datafrem.fecha_de_beneficio = pd.to_datetime(datafrem.fecha_de_beneficio,infer_datetime_format=True,errors='ignore',dayfirst=True)
    datafrem.fecha_de_beneficio = datafrem.fecha_de_beneficio.dt.strftime("%Y/%m/%d")
    datafrem.drop_duplicates(inplace = True)

    return datafrem