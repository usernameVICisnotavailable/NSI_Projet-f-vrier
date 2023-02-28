from flask import Flask, request, render_template, url_for  # import main Flask class and request object
import random
import datetime  # ne pas oublier d'importer le module datetime
import pathlib
from requests import get 
from bs4 import BeautifulSoup # Pour intégrer le nom généré aléatoirement par 'https://www.name-generator.org.uk/quick/' dans le fichier html

# ------------------------------------------------------------------------------

app1 = Flask(__name__)  # create the Flask app

# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

# cette redirection affiche la template index.html
# index.html est un fichier à créer dans un dossier templates au niveau de votre notebook
@app1.route('/', methods=['GET','POST'])
def index():
    # https://www.delftstack.com/fr/howto/python/count-the-number-of-files-in-a-directory-in-python/
    # On compte le nombre de mp3 dans le dossier 'tracks' dans 'static', puis on extrait lettre par lettre le nom de l'artiste et du titre de chaque musique qu'on enregistre respectivement dans artiste_track et titre_track, inclus dans le dictionnaire infos_track. La liste noms_tracks contient tous les dictionnaires infos_tracks, l'indice des dictionnaires correspond à l'id des divisions class="track" dans le fichier html
    noms_tracks=[]
    for path in pathlib.Path("static/tracks").iterdir():
        if path.is_file() and path.suffix == ".mp3":
            nom_musique=path.name
            artiste_track,titre_track,='',''
            for i in range(len(nom_musique)):
                carac=nom_musique[i]
                if carac=="-":
                    separation=i
            for i in range(separation):
                if nom_musique[i]=="_": # ca c'est pour remplacer les underscore par des espaces
                    carac=" "
                else:
                    carac=nom_musique[i]
                artiste_track+=carac
            for k in range(separation+1,len(nom_musique)-4): #on soustrait 4 pour que ".mp3" ne s'affiche pas après le titre
                if nom_musique[k]=="_":
                    carac=" "
                else:
                    carac=nom_musique[k]
                titre_track+=carac
            infos_track={"artiste":artiste_track,"titre":titre_track}
            noms_tracks.append(infos_track)
    
    # On effectue un tri si un e recherche a ete entree :
    displayed_tracks=[]
    if 'recherche' in request.form.keys() and request.form['recherche']!='Rechercher un titre':
        print(request.form['recherche'])
        for dict in noms_tracks:
            print(displayed_tracks)
            if request.form['recherche'] in dict['artiste'] or request.form['recherche'] in dict['titre']:
                print(dict)
                displayed_tracks.append(dict)
    else:
        displayed_tracks=noms_tracks
    print(displayed_tracks,1)

    # On cree le nombre correspondant de divisions qu'on ajoute par concatenation a 'trackdiv_list'
    trackdiv_list=''
    trackpicture_path=url_for("static",filename="images/vinyleicon.png")
    trackpicture_div=f'<div id="trackpicture"><img src="{trackpicture_path}"></div>'
    for i in range(len(displayed_tracks)):
        track_div=f'<div id="artisteinfos"><p id="nom_musique">{displayed_tracks[i]["titre"]}</p><p id="nom_artiste">{displayed_tracks[i]["artiste"]}</p></div>'
        trackdiv_list+=f'<div class="track" id="{i}">{trackpicture_div}{track_div}</div>'
    
    ########################### gérer les resultates de la barre de recherche ##############################################
    
    response = get('https://www.name-generator.org.uk/quick/')
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.select_one('.name_heading').text.strip()

    print(f"Le nom généré est : {name}")

    return render_template("index2.html",trackdiv_list=trackdiv_list,nom_profil=name)




# ------------------------------------------------------------------------------

#cette redirection récupère les données de formulaire
@app1.route("/rechercher_titre",methods = ['POST'])
def rechercher():
    result = request.form
    #a = int(result['inputa'])
    #b = int(result['inputb'])
    return result['recherche']

# ------------------------------------------------------------------------------

app1.run(port=5000)  # run app in debug mode on port 5000
