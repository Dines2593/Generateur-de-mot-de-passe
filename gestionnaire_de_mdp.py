import hashlib
import getpass

passwords ={}
mdp_clé= "NAGUnagu1908/*"

def hacheur_de_mdp(mdp):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(mdp.encode('utf_8'))
    return sha256_hash.hexdigest()

def creation_de_mdp():
    site=input("Entrez l'URL du site web : ")
    identifiant=input("Entrez votre identifiant : ")
    mdp= getpass.getpass("Entrez votre mdp : ")
    mdp_hacher= hacheur_de_mdp(mdp)
    passwords[site]= (identifiant,mdp_hacher,mdp)
    print("Mot de pass crée avec succès")
    
def recup_mdp():
    site=input("Entrez l'URL du site web : ")
    if site in passwords:
        identifiant,mdp_hacher,mdp = passwords[site]
        password= getpass.getpass("Entrez votre mdp clé : ")
        if mdp_clé == password:
            print(f" identifiant : {identifiant}")
            print(f" mot de passe : {mdp}")
        else:
            print("Mdp incorrect")
    else:
        print("Site non reconnu dans le gestionnaire de mdp")

def main():
   while True:
       print("1. Créer mon mdp")
       print("2. Récupérer mon mdp") 
       print("3.Quitter")
       choix = int(input("Entrez votre numéro correspondant à votre besoin : "))
       
       if choix == 1:
           creation_de_mdp()
       elif choix == 2:
           recup_mdp()
       elif choix == 3:
           break
       else:
           print("Choix invalide, Recommencez")

if __name__ == "__main__":
    main()
        
           