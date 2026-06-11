"""PEC4 Sergi Ortega"""

#creo dos funcions adicionals, a part de les que demana el exercici, per calcular els punts com a loval
def punts_local(resultat):
    """
    Calcula els punts que guanya l'equip local segons el resultat del partit

    Parametres:
    - resultat: resultat final del partit

    Retorna:
    - punts de l'equip local
    """
    if resultat == "H":
        return 3
    if resultat == "D":
        return 1
    return 0

#i com a visitant
def punts_visitant(resultat):
    """
    Calcula els punts que guanya l'equip visitant segons el resultat del partit

    Parametres:
    - resultat: resultat final del partit

    Retorna:
    - punts de l'equip visitant
    """
    if resultat == "A":
        return 3
    if resultat == "D":
        return 1
    return 0


def add_points(data):
    """
    Afegeix els punts de l'equip local i de l'equip visitant

    Parametres:
    - data: dataframe amb les dades dels partits i la columna FTR

    Retorna:
    - data: dataframe amb les noves columnes points_home i points_away
    """
    #utilitzo les funcions que he creat per a calcular els punts
    #creo dues noves columnes al df data
    data["points_home"] = data["FTR"].apply(punts_local)
    data["points_away"] = data["FTR"].apply(punts_visitant)
    return data


def fun_total_points(data):
    """
    Calcula els punts totals aconseguits per cada equip

    Parametres:
    - data: dataframe amb les dades dels partits i les columnes de punts

    Retorna:
    - punts_totals: llista ordenada amb els punts totals de cada equip
    """
    #agrupo tots els punts per equip de local i visitant
    punts_casa = data.groupby("HomeTeam")["points_home"].sum()
    punts_fora = data.groupby("AwayTeam")["points_away"].sum()
    #sumo tots els punts, els ordeno i poso nom al index
    punts_totals = punts_casa + punts_fora
    punts_totals = punts_totals.sort_values(ascending=False)
    punts_totals.index.name = "Equip"
    return punts_totals


def alltime_winner(punts_totals):
    """
    Retorna l'equip amb mes punts totals de tota la lliga

    Parametres:
    - punts_totals: serie amb els punts totals de cada equip ordenats de major a menor

    Retorna:
    - primer equip de la llista
    """
    #agafo el primer dela llista
    return punts_totals.head(1)