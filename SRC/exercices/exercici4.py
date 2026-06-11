"""PEC4 Sergi Ortega"""
import matplotlib.pyplot as plt
from exercices import variablesglobals as variables

def FTR(data):
    """
    Calcula el nombre de victories locals, victories visitants i empats

    Parametres:
    - data: dataframe amb les dades dels partits i la columna FTR

    Retorna:
    - ftr: dataframe amb el nombre de partits per cada tipus de resultat
    """
    #guardo quantes vegades ha guanyat el local, el visitant i sha empatat  
    ftr = data["FTR"].value_counts()
    #ho converteixo a df
    ftr = ftr.to_frame()
    #poso nom a la columna del df
    ftr.columns = ["Partits"]
    return ftr


def plot_FTR(ftr):
    """
    Crea una grafica amb els resultats finals dels partits

    Parametres:
    - ftr: dataframe amb el nombre de victories locals, victories visitants i empats

    Retorna:
    - Crea i guarda la grafica en un fitxer PNG
    """
    plt.bar(ftr.index, ftr["Partits"])
    plt.title("Resultat final dels partits")
    plt.savefig(f"src/img/ex4_resultats_partits{variables.nom_alumne}_{variables.date_time}.png")
    plt.close()