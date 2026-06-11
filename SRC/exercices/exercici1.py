"""PEC4 Sergi Ortega"""
import pandas as pd
import matplotlib.pyplot as plt
from exercices import variablesglobals as variables

def load_and_eda(fitxer):
    """
    Carrega el dataset i mostra les dades

    Parametres:
    - fitxer: ruta del fitxer CSV 

    Retorna:
    - dades: dataframe amb les dades carregades i sense algunes columnes
    """
     
    dades = pd.read_csv(fitxer)
    dades = dades.drop(columns=["HTHG", "HTAG", "HTR"])
    print("\nprimeres files del dataset:")
    print(dades.head())
    print("\nultimes files del dataset:")
    print(dades.tail())
    print("\ninformacio del dataset:")
    dades.info()
    print("\nestadistiques descriptives:")
    print(dades.describe())
    return dades

def plot_home_away_goals(dades):
    """
    Crea i  una grafica en format PNG de com es distribueixen els gols de local i visitant

    Parametres:
    - dades: dataframe amb les dades dels gols per de cada partiy

    Retorna:
    - Crea i guarda la grafica en un fitxer PNG.
    """
    plt.boxplot([dades["FTHG"], dades["FTAG"]], labels=["Gols locals", "Gols visitants"])
    plt.title("Distribucio de gols locals i visitants")
    plt.ylabel("Gols")
    plt.savefig(f"src/img/ex1_gols_locals_visitants{variables.nom_alumne}_{variables.date_time}.png")
    plt.close()