#%%
from itertools import count
from statistics import geometric_mean
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import branca 
#%%
resultados_paso = pd.read_csv(
    r"C:\Users\ivanl\OneDrive\Escritorio\MET4OP-PP3\GRUPO_GANADOR\paso_x_partido.csv" "",
    delimiter=",",  # delimitador ',',';','|','\t'
    header=0,  # número de fila como nombre de columna
    names=None,  # nombre de las columnas (ojo con header)
    index_col=0,  # que col es el índice
    usecols=None,  # que col usar. Ej: [0, 1, 2], ['foo', 'bar', 'baz']
    dtype=None,  # Tipo de col {'a': np.int32, 'b': str}
    skiprows=None,  # saltear filas al inicio
    skipfooter=0,  # saltear filas al final
    nrows=None,  # n de filas a leer
    decimal=".",  # separador de decimal. Ej: ',' para EU dat
    quotechar='"',  # char para reconocer str
    encoding=None,
)
resultados_paso
#%%
comunas = pd.read_csv(
    r"C:\Users\ivanl\OneDrive\Escritorio\MET4OP-PP3\GRUPO_GANADOR\circuitos-electorales.csv",
    delimiter=",",  # delimitador ',',';','|','\t'
    header=0,  # número de fila como nombre de columna
    names=None,  # nombre de las columnas (ojo con header)
    index_col=0,  # que col es el índice
    usecols=None,  # que col usar. Ej: [0, 1, 2], ['foo', 'bar', 'baz']
    dtype=None,  # Tipo de col {'a': np.int32, 'b': str}
    skiprows=None,  # saltear filas al inicio
    skipfooter=0,  # saltear filas al final
    nrows=None,  # n de filas a leer
    decimal=".",  # separador de decimal. Ej: ',' para EU dat
    quotechar='"',  # char para reconocer str
    encoding=None,
)
comunas
#%%
circuito_comuna = comunas[["COMUNA", "CIRCUITO_N", "BARRIO"]].rename(
    columns={"CIRCUITO_N": "circuito"}
)
circuito_comuna = circuito_comuna.sort_values(by=["circuito"])
circuito_comuna = circuito_comuna.reset_index(drop=True)

tabla_final = pd.merge(
    resultados_paso, circuito_comuna, on="circuito", how="outer", indicator=True
)
tabla_final
#%%
distrib_candidatos = (
    tabla_final[["COMUNA", "pp1", "pp2", "pp3", "pp4", "nv", "BARRIO",]]
    .groupby(["COMUNA"])
    .sum()
    .transform(lambda x: (x + 0.0) / x.sum() * 100)
)
distrib_candidatos
#%%
total_votos_x_comunas = (
    tabla_final[["COMUNA","circuito", "pp1", "pp2", "pp3", "pp4", "nv", "BARRIO"]]
    .groupby(["COMUNA","circuito"])
    .sum()
)
total_votos_x_comunas
#%%
total_votos_x_comunas = total_votos_x_comunas.assign(
    total=lambda x: (x["pp1"] + x["pp2"] + x["pp3"] + x["pp4"] + x["nv"])
)
total_votos_x_comunas
#%%
porcentaje_votos_x_comunas = total_votos_x_comunas.transform(
    (lambda x: (x + 0.0) / x["total"] * 100), axis=1
)
porcentaje_votos_x_comunas
#%%
porcentaje_votos_x_comunas.reset_index(inplace=True)
porcentaje_votos_x_comunas
#%%
porcentaje_orden = porcentaje_votos_x_comunas.sort_values(["pp3"], ascending=False)
porcentaje_orden
#%%
hogar = pd.read_csv(r"censo/hogar.csv", sep=",")
vivienda = pd.read_csv(r"censo/vivienda.csv", sep=",")
persona = pd.read_csv(r"censo/persona.csv", sep=",")
prov = pd.read_csv(r"censo/prov.csv", sep=",")
radio = pd.read_csv(r"censo/radio.csv")
frac = pd.read_csv(r"censo/frac.csv")
#%%
caba_shp = gpd.read_file(
    r"C:\Users\ivanl\OneDrive\Escritorio\VSCode\elecciones_2019\CABA.shp"
)
caba_shp["circuito"]=caba_shp["circuito"].apply(int)
caba_shp
#%%
caba_votos_shp= pd.merge(caba_shp,porcentaje_votos_x_comunas, on="circuito", how="inner")
caba_votos_shp=caba_votos_shp.sort_values("circuito")
caba_votos_shp.reset_index(inplace=True)
caba_votos_shp
#%%
caba_totales_shp= pd.merge(caba_shp,total_votos_x_comunas, on="circuito", how="inner")
caba_totales_shp=caba_totales_shp.sort_values("circuito")
caba_totales_shp.reset_index(inplace=True)
caba_totales_shp
#%%
fig, ax = plt.subplots(figsize=(10, 10))
 
# Control del título y los ejes
ax.set_title('Porcentaje de votos del partido 3 por circuito electoral', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Mostrar el mapa de %pp3
caba_votos_shp.plot(column='pp3', cmap='viridis',scheme='quantiles', k = 4, legend=True, ax=ax, zorder=5)
#%%
fig, ax = plt.subplots(figsize=(10, 10))
 
# Control del título y los ejes
ax.set_title('Porcentaje de votos del partido 3 por circuito electoral', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Mostrar el mapa de %pp3
caba_totales_shp.plot(column='pp3', cmap='viridis',scheme='quantiles', k = 4, legend=True, ax=ax, zorder=5)
#%%
import branca

colormap= branca.colormap.LinearColormap(
    vmin=caba_totales_shp["total"].quantile(0.0),
    vmax=caba_totales_shp["total"].quantile(1),
    colors=["red", "orange", "lightblue", "green", "darkgreen"],
    caption="Densidad electoral de cada circuito",
)
 
#%%
import folium
from folium.features import GeoJsonPopup, GeoJsonTooltip


m = folium.Map(location=[-34.3559, -58.2255], zoom_start=4)

popup = GeoJsonPopup(
    fields=["circuito", "pp3"],
    aliases=["Nº Circuito: ", "Votos PP3: "],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

tooltip = GeoJsonTooltip(
    fields=["departamen", "circuito", "total", "pp3", "nv"],
    aliases=["Comuna:", "Nº Circuito:", "Votos totales: ", "Votos de PP3: ", "Votos NV"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)


g = folium.GeoJson(
    caba_totales_shp,
    style_function=lambda x: {
        "fillColor": colormap(x["properties"]["total"])
        if x["properties"]["pp3"] is not None
        else "transparent",
        "color": "black",
        "fillOpacity": 0.4,
    },
    tooltip=tooltip,
    popup=popup,
).add_to(m)

colormap.add_to(m)

m
#%%
caba_votos_shp.explore( column="circuito", # make choropleth based on "BoroName" column
     tooltip= "pp3", # show "BoroName" value in tooltip (on hover)
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set3",
     style_kwds=dict(color="black"),
) 
#%%

#%%
ax.set_title('Porcentaje de votos no válidos por circuito electoral', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Mostrar el mapa finalizado
caba_votos_shp.plot(column='nv', cmap='viridis',scheme='quantiles', k = 4, legend=True, ax=ax, zorder=5)
#%%
import folium
from folium.features import GeoJsonPopup, GeoJsonTooltip


m = folium.Map(location=[-34.3559, -58.2255], zoom_start=4)
m
#%%
