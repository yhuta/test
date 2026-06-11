"""PEC4 Sergi Ortega"""
import matplotlib.pyplot as plt
from exercices import variablesglobals as variables

def goals_distribution(dades):
    """
    Calcula la distribucio de gols marcats pels equips locals i visitants

    Parametres:
    - dades: dataframe amb les dades dels partits i les columnes de gols.

    Retorna:
    - distr_goals_home: dataframe amb la quantitat de partits segons els gols locals
    - distr_goals_away: dataframe amb la quantitat de partits segons els gols visitants
    """
    #calculo quantes vegades s'han marcat un numero de gols i ho ordeno
    distr_goals_home = dades["FTHG"].value_counts().sort_index()
    distr_goals_away = dades["FTAG"].value_counts().sort_index()
    #ho converteixo a df
    distr_goals_home = distr_goals_home.to_frame()
    distr_goals_away = distr_goals_away.to_frame()
    #poso noms a les colunesd els df
    distr_goals_home.columns = ["Partits"]
    distr_goals_away.columns = ["Partits"]
    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    """
    Crea una grafica amb la distribucio de gols locals i visitants

    Parametres:
    - distr_goals_home: dataframe amb la distribucio de gols marcats pels equips locals
    - distr_goals_away: dataframe amb la distribucio de gols marcats pels equips visitants

    Retorna:
    - Crea i guarda la grafica en un fitxer PNG
    """
    plt.plot(distr_goals_home.index, distr_goals_home["Partits"], label="Gols locals")
    plt.plot(distr_goals_away.index, distr_goals_away["Partits"], label="Gols visitants")
    plt.title("Distribucio de gols")
    plt.legend()
    plt.savefig(f"src/img/ex3_distribucio_gols{variables.nom_alumne}_{variables.date_time}.png")
    plt.close()