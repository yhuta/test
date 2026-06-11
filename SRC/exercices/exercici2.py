"""PEC4 Sergi Ortega"""
import matplotlib.pyplot as plt
from exercices import variablesglobals as variables

def total_matches(dades):
    """
    Calcula el nombre total de partits jugats per equip 

    Parametres:
    - dades: dataframe amb les dades dels partits de la lliga

    Retorna:
    - matches_team_total: un nou dataframe amb el nombre total de partits jugats per cada equip
    """
    #contem quants partits ha jugat cada equip com a local i visitant
    partits_casa = dades["HomeTeam"].value_counts()
    partits_fora = dades["AwayTeam"].value_counts()
    #els sumem
    partits_totals = partits_casa + partits_fora
    partits_totals = partits_totals.sort_values(ascending=False)
    matches_team_total = partits_totals.reset_index()
    matches_team_total.columns = ["Equip", "Partits"]
    return matches_team_total


def plot_matches_team_total(matches_team_total):
    """
    Crea una grafica amb el nombre total de partits jugats per cada equip

    Parametres:
    - matches_team_total: dataframe amb els equips i el numero total de partits jugats

    Retorna:
    - Crea i guarda la grafica en un fitxer PNG
    """
    #utilitzo el nou df que he creat per agafar les dades
    plt.bar(matches_team_total["Equip"], matches_team_total["Partits"])
    plt.title("Partits totals jugats per equip")
    #roto 90 grraus els noms del equips per que es vegin
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f"src/img/ex2_partits_totals{variables.nom_alumne}_{variables.date_time}.png")
    plt.close()