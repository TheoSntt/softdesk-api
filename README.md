
# API SOFTDESK


## Avertissements

Ce repo contient l'API de suivi de problèmes de SoftDesk.
Il s'agit d'un projet exercice du cursur OpenClassrooms.

## Mise en place et exécution en local de l'API

1. Téléchargez le projet depuis Github. Soit directement (format zip), soit en clonant le projet en utilisant la commande suivante dans Git Bash :  
```
git clone https://github.com/TheoSntt/OC_Project_10
```
2. Créez un environnement virtuel Python en exécutant la commande suivantes dans le Terminal de votre choix :
```
python -m venv env (env étant le nom de l'environnement, vous pouvez le changer)
```
Puis, toujours dans le terminal, activez votre environnement avec la commande suivante si vous êtes sous Linux :
```
source env/bin/activate
```
Ou bien celle-ci si vous êtes sous Windows
```
env/Scripts/activate.bat
```
3. Dans vorte environnement virtuel, téléchargez les packages Python nécessaires à la bonne exécution de l'application à l'aide de la commande suivante :
```
pip install -r requirements.txt
```
NB : Puisque la BDD n'est incluse dans le répo, il est nécessaire de procéder aux migrations. Pour créer la BDD en local, procédez aux migrations, à l'aide de la commande suivante :
```		
python manage.py migrate
```
4. Vous pouvez maintenant exécuter l'API en local. Il vous suffit de lancer le serveur local, à l'aide de la commande suivante :
```		
python manage.py runserver
```
5. L'API est prête à être utilisée. Son fonctionnement correspond aux documents de conception fournis.
 
 
 
 POUR PLUS D'INFORMATION SUR LE FONCTIONNEMENT DE L'API : La documentation complète de l'API est disponible à l'adresse suivante :
```		
https://documenter.getpostman.com/view/27582538/2s93mAUzwo
```
