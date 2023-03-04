from flask import Flask, request, render_template, url_for  # import main Flask class and request object
import pathlib
from requests import get 
from bs4 import BeautifulSoup # Pour intégrer le nom généré aléatoirement par 'https://www.name-generator.org.uk/quick/' dans le fichier html
import csv

# ------------------------------------------------------------------------------

app1 = Flask(__name__)  # create the Flask app

# ------------------------------------------------------------------------------


# cette redirection affiche la template index.html
# index.html est un fichier à créer dans un dossier templates au niveau de votre notebook
@app1.route('/', methods=['GET','POST'])
def index():
    global name
    
    ##################################### GESTION DES COMMENTAIRES #####################################
    commentaires=[]
    with open("static/commentaires.csv", mode="r") as fichier_r:        #"w" signifie que nous voulons écrire dans le fichier. On utilise le gestionnaire de contexte with pour nous assurer que le fichier est fermé proprement une fois que nous avons fini de l'utiliser
        lecteur_csv = csv.reader(fichier_r, delimiter=',')
        for comm in lecteur_csv:
            commentaire=""
            for lettre in comm:
                commentaire+=lettre #On ajoute lettre par lettre le commentaire comm à la variable de type string par concaténation
            commentaires.append(commentaire) #"commentaires" est donc la liste des tous les commentaires "commentaire"
    if 'nouveau_commentaire' in request.form.keys():   #condition : un formulaire de commentaire à été envoyé
        print(f"{name} à commenté : {request.form['nouveau_commentaire']}")
        ccc=''
        ccc+=request.form['nouveau_commentaire']
        ccc+=f' - {name}'     #On ajoute par concaténation le nouveau commentaire à la variable string ccc, puis on ajoute " - nom de l'utilisateur qui à posté le commentaire" à la fin
        commentaires.append(ccc)   #On ajoute ce nouveau commentaire à la liste des commentaires
        with open("static/commentaires.csv", mode="w", newline="") as fichier_w:        #On écrit "w" parce que nous sommes en écrite (write)
            writer = csv.writer(fichier_w)
            for c in commentaires:
                writer.writerow(c)

    commentlist=''    #La variable string qui va contenir le programme html que l'on va introduire dans le fichier html
    for i in range(len(commentaires)):
        commentlist += f"<div class='comment'>{commentaires[len(commentaires)-i-1]}</div>" # on utilise cette méthode avec l'indice pour que les commentaires s'affiche dans l'ordre du plus récent en haut
    
    ##################################### AFFICHAGE DES MUSIQUES #####################################
    # https://www.delftstack.com/fr/howto/python/count-the-number-of-files-in-a-directory-in-python/
    # On compte le nombre de mp3 dans le dossier 'tracks' dans 'static', puis on extrait lettre par lettre le nom de l'artiste et du titre de chaque musique qu'on enregistre respectivement dans artiste_track et titre_track, inclus dans le dictionnaire infos_track. La liste noms_tracks contient tous les dictionnaires infos_tracks, l'indice des dictionnaires correspond à l'id des divisions class="track" dans le fichier html
    noms_tracks=[]  #deviendra une liste de dictionnaires correspondant chacun à une musique (les clés sont 'artiste','titre' et 'fichier', cette dernière correspondant au nom exacte du fichier)
    for path in pathlib.Path("static/tracks").iterdir():
        if path.is_file() and path.suffix == ".mp3":
            nom_musique=path.name
            artiste_track,titre_track,='',''
            for i in range(len(nom_musique)):
                carac=nom_musique[i]
                if carac=="-":   #tiret séparant le nom de l'artiste du nom de la musique détecté
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
            infos_track={"artiste":artiste_track,"titre":titre_track,"fichier":path.name}
            noms_tracks.append(infos_track)
    # On effectue un tri si une recherche a ete entree :
    displayed_tracks=[]
    if 'recherche' in request.form.keys():
        print(f"{name} à recherché : {request.form['recherche']}")
        for dict in noms_tracks:
            if request.form['recherche'].lower() in dict['artiste'].lower() or request.form['recherche'].lower() in dict['titre'].lower():
                displayed_tracks.append(dict)
    else:  #sinon les musiques affichées sont les mêmes que celles dans le fichier tracks
        displayed_tracks=noms_tracks
    print(displayed_tracks)
    # On cree le nombre correspondant de divisions qu'on ajoute par concatenation a 'trackdiv_list'
    trackdiv_list=''
    trackpicture_path=url_for("static",filename="images/vinyleicon.png")
    for i in range(len(displayed_tracks)):
        lien_bouton=url_for("static",filename=f"tracks/{displayed_tracks[i]['fichier']}")
        trackpicture_div=f'<div id="trackpicture"><a href="{lien_bouton}" target="_blank"><button id="bouton_musique"><img src="{trackpicture_path}"></button></a></div>'
        track_div=f'<div id="artisteinfos"><p id="nom_musique">{displayed_tracks[i]["titre"]}</p><p id="nom_artiste">{displayed_tracks[i]["artiste"]}</p></div>'
        trackdiv_list+=f'<div class="track" id="{i}">{trackpicture_div}{track_div}</div>'
    
    ########################### GENERATION DU NOM DE PROFIL ##############################################
    
    response = get('https://www.name-generator.org.uk/quick/') # envoie une requête http get à l'url inscrit, et stocke la réponse dans la variable reponse
    soup = BeautifulSoup(response.text, 'html.parser')     # 'html.parser' est un 'parseur' intégré à la bibliothèque standard de Python et permet d'analyser le contenu HTML récupéré par la requête http get
    name = soup.select_one('.name_heading').text.strip() #select_one permet de prendre le contenu de la première balise .name_heading de la page (qui contient le nom), strip permet de supprimer les espaces superflus au début et à la fin de la chaine

    ##########################################################################
    return render_template("index.html",trackdiv_list=trackdiv_list,nom_profil=name,commentlist=commentlist)




# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

app1.run(port=5000)  # run app in debug mode on port 5000
