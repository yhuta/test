"""PEC4 Sergi Ortega"""


#exercici 1
from exercices.exercici1 import load_and_eda, plot_home_away_goals

file = "SRC/data/LaLiga_Matches.csv"
data = load_and_eda(file)
plot_home_away_goals(data)

#exercici 2
from exercices.exercici2 import total_matches, plot_matches_team_total

matches_team_total = total_matches(data)
plot_matches_team_total(matches_team_total)

#exercici 3
from exercices.exercici3 import goals_distribution, plot_goals_distribution

gols_casa, gols_fora = goals_distribution(data)
print(gols_casa)
print(gols_fora)
plot_goals_distribution(gols_casa, gols_fora)

#exercici 4
from exercices.exercici4 import FTR, plot_FTR

ftr = FTR(data)
print(ftr)
percentatge = ftr.loc["H", "Partits"] / ftr["Partits"].sum() * 100
print("Percentatge de partits guanyats pels locals:")
print(percentatge)
plot_FTR(ftr)

#exercici 5
from exercices.exercici5 import add_points, fun_total_points, alltime_winner

data = add_points(data)
print(data.head(10))
punts_totals = fun_total_points(data)
print(punts_totals.head(10))
guanyador = alltime_winner(punts_totals)
print("Guanyador històric:")
print(guanyador)
