# Scrapping des données des parkings de la ville de Montpellier
## Introduction : 
## Notre projet consiste à récupérer en temps réel les données des **parkings routiers** de la ville de Montpellier ainsi que les utilisations des **stations de vélo** de cette même ville pour analyser l'influence entre les deux. 
## Pour ceci, nous avons écrit des scripts python qui récupère les données mesurées en quasi temps réel ( toutes les 5-10 minutes ) de l'activité des parkings routier ainsi que ceux pour les vélos, qui sont disponibles sur le site ***data.montpellier3m.fr***.
## Finalement, un script bash s'occupera d'actualiser notre Github automatiquement avec les nouvelles données chaque heure, ce qui aura pour conséquence d'actualiser notre site Internet en affichant et sauvegardant les nouvelles valeurs ainsi que les anciennes.

----
# Notre réalisation : 
![capturecode](captures/Capture.JPG)
*extrait de notre code*
## Ci-dessus, vous pouvez entrevoir un bout de notre code Python qui nous permet de récupérer les données afin de les stocker dans plusieurs fichiers que nous allons expliquer au fur et à mesure.
## Le code marche de cette manière : 
>* ## Il récupère les **données** de **chaque parking** sous format **xml**
>* ## Il les **classe** ensuite dans un dossier nommé **'data'**
>* ## Il va ensuite **récupèrer** les valeurs précises (comme le nombre de places libres,totales...) dans les fichiers à l'intérieur du dossier data
>* ## Il va faire un **résumé** pour **chaque parking** de ce qu'il a récupérer et va l'**écrire dans un nouveau fichier texte stocké dans le dossier 'scrap' avec comme nom la date et l'heure du scrapping.** *Cela nous sert à comprendre les données pour vérifier les éventuelles erreurs.*
>* ## Finalement, il va **stocker** dans un nouveau fichier stocké dans le dossier 'data_graph' et qui nous servira réellement **pour l'évaluation de l'utilisation des différents parkings**
>* ## Avec les données récoltés, un **graphique** (*produit avec GnuPlot*) se crée **en temps réel** et **s'actualise toutes les 24h** (*crée un autre graphique pour chaque jours*)
>* ## Finalement, un script bash actualisera les données sur le Github principal et les valeurs ainsi que le graphique qui se trace au fur et à mesure, s'affiche sur notre site Internet.
## Il est important de noter que, pour créer les graphiques, nous avons choisi d'utiliser le **taux d'occupation des parkings routiers et le taux d'utilisation de vélos** **pour toute la ville**.
## Et enfin, **le programme se relance toutes les 24h en entier** et **récupère des données toutes les heures**, pour éviter les **problèmes d'actualisation** qu'on peut avoir avec le site d'OpenData.
-----
# Proof of Concept
## Exemple d'un fichier XML récupéré : 
![xml](captures/ex1.JPG)
## Exemple d'un 'résumé' de scrapping : 
![resume](captures/ex2.JPG)
## Exemple des données récoltés pour le graphique : 
![graph](captures/ex3.JPG)
## Exemple de résultat final pour le graphique avec *GnuPlot* :
![gpra](captures/ex4.JPG)  

---- 
# Détails techniques 
## Pour le graphique avec gnuplot, nous avons choisi les options suivantes (Ces options sont incluses dans notre script bash et ainsi les programmes finaux se veulent polyvalent et executables sur n'importe quelle machine avec Linux) : 
    set xrange [0:23] # Abscisse qui représente les heures de la journée
    set yrange [0:100] # Ordonnée qui représente le taux de pourcentage (donc entre 0 et 100%)
    set title"Taux d'occupation des parkings | Taux d'utilisation des vélos" # Pour le titre du graphique
    set xlabel "Temps ( en heure )" # Titre abscisse
    set ylabel "Taux ( en % )" # Titre ordonnée
    set term jpeg # Pour sortir en image sous format .jpeg
    set output "photo_graph/graph.jpeg"  # Où on stocke l'image qui en sort
## Et finalement, pour tracer le graphique :
    plot "$HOME/Data-Scrapping-Montpellier/data_graph/voiture_velo.dat" using 1:2 title"Taux d'occupation des parkings routiers" linewidth 2 with lines, "$HOME/Data-Scrapping-Montpellier/data_graph/voiture_velo.dat" using 1:3 title"Taux d'utilisation des velos" linewidth 2 with lines

-----
# Optimisations et améliorations :
## Nous voulons approfondir un peu plus notre projet en rajoutant :
* ## La création de **graphiques pour chaque parking**
* ## Des **graphiques plus précis et poussés** en prenant en compte la **localisation des parkings vélos proches de chaque parking routiers** pour confirmer la véritable corrélation Occupation parking/Utilisation des vélos

----
# Notes : 
* ## Le programme n'est pas encore totalement fonctionnel (Il manque le git push automatique)
* ## Il faudrait également beaucoup plus de temps pour pouvoir mesurer sur de longues périodes pour avoir des conclusions plus pertinentes et précises.
