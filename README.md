# accident-velo-2020-France
Visualisation des accidents de vélo en France &amp; DOM-TOM en 2020


A partir des données disponibles sur data gouv : https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/

J'ai créé une BDD à l'aide de SQL3. Voir fichier create_db.py. Les données étaient partagées en 4 fichiers csv. Dans le fichier populate_db.py, j'utilise ces fichiers pour remplir les BDD. 
Puis en utilisant FastAPI, j'ai développé une Webapp. Elle permet de trier les résultats par niveau de gravité.
Les tableaux ainsi que la carte sont mise à jour dynamiquement en effectuant des requêtes SQL en arrière fond. La carte repose sur Folium et fonctionne également à partir de la BDD.

J'ai déployé la webapp sur heroku. Vous pouvez la consulter à l'adresse suivante: https://accident-velo-2020.herokuapp.com/
