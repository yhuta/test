PEC4 - Anàlisi LaLiga 1995-2020
Sergi Ortega Pons

Descripció del projecte

Es tracta de la última práctica de l'assignatura 22.503 - Programación para la ciencia de datos.

La finalitat de la práctica és treballar amb un dataset real, descarregat a la página web kaggle.com, que conté dades dels partits de LaLiga des de l'any 1995 fins al 2020.

S'han de treballar les dades seguint les pautes marcades per una serie d'exercicis, per tal d'obtenir dades i gráfiques analitzables.

Estructura del projecte

PEC4 

Entorn virtual

Per a executar el projecte es rocomana utilitzar un entorn virtual, així només s'instalen les llibreries, o modifiquen versions dins d'aquest entorn, i no modifica altres projecte.

Per crear l'entorn virtual s'ha dexecutar el seguent comandametn 
python -m venv venv

Per activar-lo en Windows PowerShell:
venv\Scripts\activate

Per sortir de l’entorn virtual:
deactivate

Instal·lació de llibreries

Les llibreries necesaries amb la seva versió corresponent están a requeriments.txt.
Per instalarles cal executar el comendament pip install -r requirements.txt
Les llibreries son pandas i matplotlib.

Execució del projecte

Primerament cal situarse a la carpeta arrel del projecte.
Amb l'entorn virtual activat executar: python SRC/main.py
Les gràfiques generades es guarden dins de la carpeta SRC/img.

Comprovació de l’anàlisi estàtic (linting)

Per comprovar el codi amb pylint cal executar: pylint SRC
Aixi obtenim el linting de tots els continguts dins de SRC.

Generació de documentació

Per a generar la documentació utilitzant pydoc, ho hem de fer exercici a exercici executant: python -m pydoc -w SRC.exercices.exercici1

Els arxius .html es creen dins de la carpeta arrel, s'han de guardar a la carptea doc. Es poden obrir des de la carpeta del projecte, fent doble clic. S'obren al navegador predeterminat.

License

Aquest projecte té un arxiu License, que consisteix en una llicéncia MIT.


Comandes per pujar el projecte a Github

Executem git init per iniciar github.
Executem git status per veure el estat dels arxius, quins estan pujats i quins no.
Executem git add + el nom del archiu que volem penjar.
Executem git add . si volem afegir tots els canvis realitzats.
Executem git commit -m "UN NOM QUE VULGUEM" per guardar els canvis.
Executem git log per veure el registre de commits.

