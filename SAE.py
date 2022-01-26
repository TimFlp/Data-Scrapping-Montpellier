from urllib import request
import requests
from lxml import etree
from time import gmtime, strftime , sleep
from datetime import datetime

f1 = open('data_graph/voiture_velo.dat','w',encoding='utf8')
f1.close()

def velo_msj():
    total = 0
    free = 0
    req=(requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")).text
    nom_complet4 = 'data/VELOMAG'
    f1=open(nom_complet4,'w',encoding='utf-8')
    f1.write(req)
    f1.close()
    nom_complet5 = 'scrap/result_velo'
    f2=open(nom_complet5,"w",encoding='utf-8')
    tree=etree.parse(nom_complet4)
    for si in tree.xpath("/vcs/sl/si"):
        fr=si.get('fr')
        free += int(fr)
        tot=si.get('to')
        total += int(tot)
        f2.write(fr+'\n')
    f2.close()
    taux_occup = int(((total-free)*100)/total)
    print(str(taux_occup))
    return str(taux_occup)

def velo_tot(taux_occup):
    #print('total : ',total,"\nfree : ",free,"\ntaux d'occupation : ",taux_occup,'%')
    f=open('data_graph/voiture_velo.dat','r',encoding='utf8')
    b = f.read()
    f.close
    f=open('data_graph/voiture_velo.dat','a',encoding='utf8',newline='')
    f.write(b +' '+taux_occup+'\n')
    f.close()
    print("velo_tot")
    return None
    
parkings=["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC","FR_MTP_SABL","FR_MTP_MOSS","FR_STJ_SJLC","FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109","FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE",'FR_MTP_POLY']


def voiture_msj():

    for i in range(len(parkings)): # On récupère la page entière au format XML et on en crée un fichier pour chaque avec les données à l'intérieur.
        print("Récupérations des données pour le parking suivant : ",parkings[i])
        url = "https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml" # Génération du lien en fonction du code de parkings.
        response = requests.get(url)
        nom_complet = 'data/'+str(parkings[i])
        f1=open(nom_complet,"w", encoding='utf8')
        f1.write(response.text) # On écrit dans le fichier toute la page qu'on a récupérer.
        f1.close()

    fr=0 # Variable utile pour calculer le taux de place occupé dans la ville en entière
    tot=0 # Même role
    date = datetime.now() # On sauvegarde la date du scrapping 
    date = str(date)[:13]+"-"+str(date)[14:16]+"-"+str(date)[17:19] # Etape nécessaire pour enlever les : qui sont des caractères interdits pour sauvegarder des fichiers. 
    nom_complet2 = 'scrap/'+str(date)
    f1=open(nom_complet2,"w",encoding='utf8') # On donne en titre à notre fichier la date du jour et l'heure.
    f1.write(date+"\n")

    for i in range(len(parkings)):
        nom_complet3 = 'data/'+parkings[i]
        tree = etree.parse(nom_complet3)
        for statut in tree.xpath("Status"): # Récupération de l'état du parking (Ouvert ou fermé).
            if statut.text == 'Open': 
                for total in tree.xpath("Total"): # Récupération du nombres des places totales disponibles. 
                    total = int(total.text)
                    tot += total
                for nom in tree.xpath("Name"): # Récupération du nom du parking en entier.
                    f1.write('Nom du parking : '+nom.text)
                for libre in tree.xpath("Free"): # Récupération du nombre de places libres disponibles.
                    free = int(libre.text)
                    fr += free
                    f1.write('  Nombre de places libres : '+str(free))
                pour_place_occupe_park = int((total-free)*100/total) # Calcul du taux de place occupés pour le parking.
                print('% places occupées pour le parking',parkings[i]," : ",pour_place_occupe_park,"%")
                f1.write('  Taux de places occupées : '+str(pour_place_occupe_park)+'\n')
            else:
                for nom in tree.xpath("Name"): # Si le parking est écrit comme fermé, alors on écrit dans le récapitulatif qu'il est fermé
                    print("Parking :",nom.text,"fermé!")
                    f1.write("\nParking : "+nom.text+" fermé!\n")       
      
    f1.close()
    print(str(int((tot-fr)*100/tot)))
    return str(int((tot-fr)*100/tot))

def voiture_tot(tot,h):
    f=open('data_graph/voiture_velo.dat','r',encoding='utf8')
    b = f.read()
    f.close
    f=open('data_graph/voiture_velo.dat','a',encoding='utf8',newline='')
    if b=='':
        f.write(str(h)+' '+tot)
    else:
        f.write(b+str(h)+' '+tot)
    f.close()
    print('voiture_tot')
    return None

def lancement(h):
    if h ==24:
        return None

    voiture = voiture_msj()
    voiture_tot(voiture,h)
    velo = velo_msj()
    velo_tot(velo)
    sleep(60*60)
    print(h)

    return lancement(h+1)

lancement(0)