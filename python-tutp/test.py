print("hello world")

for i in range(10):
    if i % 2 == 0:
        print(i)

word = "hello"
word2 = "world"

print(word+" "+word2)


#créer un environnement virtuel
#virtualenv -p python3 .venv
#l'activer 
#source .venv/bin/activate
# désactiver -- deactivate
## commande permettant de mettre dans un fichier toutes les librairies à installer
#pip freeze > requirements.txt
#installer les librairies présentes dans les requirements
#pip install -r requirements