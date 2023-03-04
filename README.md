# NSI_Projet-fevrier
Un site qui indexe des .mp3 facilement téléchargeables enregistrés dans un dossier du serveur flask.
Groupe : Celia Mazet (CMZ)/Samy Hammouche (SHM)/Victor Le Peillet (VLP)

! CLIQUER SUR "MODIFIER" POUR LIRE CE FICHIER !  
          (le bouton crayon)

VLP : Premiers pas avec le serveur en flask : tests et appropriation du notebook jupyter. Reamarque : impossible de recharger le fichier css un fois le serveur lancé          (même en arrêtant le noyaux, en fermant jupyter, et en supprimant le fichier css !)                           (21/02 : 15h20-->17h30)
     Création des premières versions de index.html et de style.css (fonctionnement hors ligne car problème de chargement du css avec le serveur, il suffit de d'ouvrir         le fichier .html dans le navigateur)                                                                          (22/03 : 12h20-->18h15)
     v2 : ajout de fonctionnalités dans le volet de gauche et création des divisions track qui seront intégrées dans le serveur. Version qui ne fonctionne pas avec            serveur, à exécuter en local uniquement.                                                                      (24/02 : 7h-->9h/18h45-->~21h)
     Mise en marche et développement du serveur (compréhension du fonctionnement, relier le fichier css ...)         (24/02 : ~22h-->00h10)
     v3 : Mise en place du serveur (j'ai copié-collé les cellules du notebook jupyter dans un fichier python, attention ne pas oublier d'importer en pip install les           librairies spécifiées au début du fichier 'flask_server3.py': vous tapez sur internet le nom de la librairie avec pip install, puis vous cliquez sur le site           pypi.org, vous copiez la commande et vous la collez dans votre invite de commande, n'oubliez pas de redémarrer éventuelement votre IDE pour que les changements         s'appliquent). 
        Barre de recherche des titres fonctionnelle (recherche dans les noms des musiques et des artistes.
        Pour ajouter un titre : mettez le fichier mp3 dans le dossier tracks : ATTENTION DE BIEN NOMMER LE FICHIER : nom_de_l'artiste-nom_de_l'auteur.mp3 (sinon ça             marche pas).
        ATTENTION A BIEN RANGER LES FICHIERS DANS LES BONS DOSSIERS : vous mettez le fichier python flask dans un dossier (de préférence vide), le (ou les) fichier             html dans un sous-dossier 'templates', le fichier css ou javascript dans un sous-dossier 'static', et enfin les .mp3 dans un sous-dossier 'tracks' dans le sous         dossier 'static', ainsi que les images dans le sous-dossier 'images' dans le sous-dossier 'static'.
        --static
        ----.css
        ----.js
        ----tracks
        ------.mp3
        ------...
        ----images
        ------.png
        --templates
        ----.html
        --.py
        Le volet de gauche avec les commentaires et le lien du mp3 n'est pas encore fonctionnel, il faut le relier avec le serveur et un fichier javascript qui                 détecterait lorsque l'utilisateur clique sur une <div class='tracks'>. Je me suis dit que peut-être qu'on pourrait ne pas le faire et afficher directement          le lien du fichier .mp3 dans la <div class='tracks'>
        La photo de profil est maintenant de service : elle change à chaque fois qu'on recharge la page, ainsi que le nom.   
                                                                                (25/02 : 21h30-->1H20, 26/02 : 13h30-->16h50/20h00-->00h10,27/02 : 21h30 --> 00h50)
                                                                                
                                                                                
                                                                                
                                                                                
                                                        
                                           
CMZ : recherches sur le fonctionnement de flask, rattrapage des cours manqués à cause de l'échange, notamment grâce au notebook( 22/02: 14h-->18h).
j'ai installé VScode, étudié le code commencé par Victor. pb, je n'arrives pas à afficher la page wb avec un moteur de recherche. (27/02: 14h30-->16h30).

VLP & CMZ : Ajout des noms dans les commentaires, Amélioration du visuel des div 'track', cliquer sur l'image de vinyle mène au fichier, lors de la recherche d'un titre, les résultats s'affiche sans tenir compte de la mise en majuscule de certaines lettres (10h00 --> 15h00 + 47 minutes)
