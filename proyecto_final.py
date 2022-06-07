# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:43:17 2022

@author: fedrapineda
"""

#Karina Pérez
#Fedra Pineda

#Para descargar la base de datos es necesario usar la API de Yahoo Finance 
#para eso se debe usar el comando "pip install yfinance" s—lo una vez.

#pip install yfinance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import csv
import seaborn as sns #PARA GRAFICA DE CORRELACIONES


#Base 1:Precios de las empresas

tickers= list(("REP.MC", "ELE.MC", "IBE.MC", "ENG.MC", "REE.MC", "ABG.MC", "PBR", "GAZP.ME", "XOM", "CVX", "PTR"))
empresas= yf.download(tickers,period="1m", start= "2005-01-01", end= "2021-12-01")

cierre= pd.DataFrame(empresas.dropna(thresh=0, axis= 1)["Close"]).dropna()

cierre.index.names= ["Fecha"]

#Datos mensuales
cierre= cierre.resample("M").mean()

#asignamos indices 
cierre=cierre.assign(profit=range(0,141)) #asignamos un indice
empresas_final=cierre.set_index("profit")



#Base 2: inflación no subyacente
data=pd.read_csv("Inflación_nosubyacente_anual.csv")
DATAF9=pd.DataFrame(data).dropna()

final=data.loc[326:466] #selecciono las los datos  que coinciden con la base cierre: del 03-2011 al 11-2021


final2=final.assign(profit=range(0,141)) #asignamos un indice
inflacion=final2.set_index("profit")


#unimos bases 
Combinacion= pd.concat([empresas_final, inflacion],axis=1)
Combinacion.columns.values



#Gráficas: Correlaciones
ax1 = sns.lmplot(x='ABG.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Abengoa S.A: precio de la acción e inflación no subyacente', fontsize = 16);


ax2 = sns.lmplot(x='CVX', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Chevron Corporation: precio de la acción e la inflación no subyacente', fontsize = 16);



ax3 = sns.lmplot(x='ELE.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Endesa S A: precio de la acción e la inflación no subyacente', fontsize = 16);



ax4 = sns.lmplot(x='ENG.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Enagás S A: precio de la acción e la inflación no subyacente', fontsize = 16);




ax5 = sns.lmplot(x='GAZP.ME', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Public Joint Stock Company Gazprom: precio de la acción e la inflación no subyacente', fontsize = 16);



ax6 = sns.lmplot(x='IBE.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Iberdrola S A : precio de la acción e la inflación no subyacente', fontsize = 16);


ax7 = sns.lmplot(x='PBR', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Petróleo Brasileiro S A -Petrobras: precio de la acción e la inflación no subyacente', fontsize = 16);



ax8 = sns.lmplot(x='PTR', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('PetroChina Company Limited: precio de la acción e la inflación no subyacente', fontsize = 16);



ax9 = sns.lmplot(x='REE.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Red Eléctrica Corporation: precio de la acción e la inflación no subyacente', fontsize = 16);




ax10 = sns.lmplot(x='REP.MC', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Repsol S A : precio de la acción e la inflación no subyacente', fontsize = 16);


ax11 = sns.lmplot(x='XOM', y='Inflacion_nsubyacente', data=Combinacion, line_kws={'color': 'lightsalmon'},height=7);
plt.xlabel("Precio", fontsize = 13);
plt.ylabel("UDIS", fontsize = 13);
plt.title('Exxon Mobil Corporation: precio de la acción e la inflación no subyacente', fontsize = 16);


