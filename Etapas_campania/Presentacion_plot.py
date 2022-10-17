#%%
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
import numpy as np
#%%
votos = gpd.read_file("/Users/macbook/Desktop/VS_Code/Ejercicios/ExperimentoPandas/elecciones_2019/CABA.shp"
)
votos.explore() #Magia, es el mapa interactivo
#%%
votos['logRatio'] = (votos.indec_d/ votos.geometry) #No estaria funcionando
votos.plot(column='logRatio', scheme='quantiles', figsize=(10, 10))
# %%
df_votos = pd.DataFrame(votos)
print(df_votos)
# %%
df_votos.columns()
#%%
votos.plot(column = "departamen")
#%%