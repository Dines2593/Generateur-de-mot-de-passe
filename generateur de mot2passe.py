import random
import string 

print ('Generateur de Mot de passe')

majuscules = string.ascii_uppercase
minuscules = string.ascii_lowercase
chiffres = string.digits 
caracteres_space = ''


  

nbdemdp = input('Nombre de mot de Passe qur vous voulez generer: ')
nbdemdp = int(nbdemdp)
longeurdumdp = input('Longeur du mot de Passe qur vous voulez generer: ')
longeurdumdp = int(longeurdumdp)
besoin_de_caractere_space = input('Avez vous besoin de caratères spéciaux dans vos mots de passe (0 pour non 1 pour oui) ')



if besoin_de_caractere_space == '1':
    caracteres_space = string.punctuation 

categorie = [majuscules, minuscules, chiffres, caracteres_space] #liste de variables contenant tous les caracteres 

print('\nVoici vos mots de passe')

for pwd in range(nbdemdp):
        mot_de_passe = []
        for _ in range(longeurdumdp):
            categorie_choisy = random.choice(categorie)
            mot_de_passe.append(random.choice(categorie_choisy)) #append sert ici à rajouter l'occurence à la fin de la liste 

        mot_de_passe = ''.join(mot_de_passe) #fusionner les occurences de la liste pour former le mdp 
        print(mot_de_passe)

    
