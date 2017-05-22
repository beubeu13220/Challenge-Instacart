# Challenge-Instacart


* Remarque 1 :
Par rapport à la table order, la distribution sur les variables de order sont les mêmes pour le train et le test 

* Remarque 2 :
Observer si les commandes réalisée dans un délai plus court que habituellement, ou si la commande a lieu un jour inabituel si il y'a des reoder.
En effet commander un jours après une prècédente commande peut concerner un oublie 

* Remarque 3 :
Order_products_train ne contient que des commandes des commande id qui ont un eval_set à "train"

* Remarque 4 : 
si j'achete deux fois le même produit et que j'en recommande un ?
comment cela se passe ? 
On confirme qu'il ny'a pas de reordered lors de la première commande 

## stat descriptive order products donc faire un concat entre le train et le prior

1. Le nombre de produit commandé par commande
2. Le nombre de reoder par commande 
3. Nombre produit/ nombre reoder selon le jour l'heure et l'espacement avec précédente commande
4. Le type de produit reoder 
5. le taux de reordered
6. le type de produit reoder selon le jour l'heure et l'espacement avec précédente commande

=> faire ses stats avec le merge du train et du prior  
=> faire ses stats que sur le prior

faire des stats sur le lien entre le train et le order 


## Idée d'approche :

	- Créer des clusters de produit, selon leur caractéristique et si ils sont commandé ensemble
	- Ensuite prédire la commande ou non de ces clusters
	- regarder les produits toujours re commandé ou jamais recommande une fois commandé
	- regarder si il y'a des ID dans le test qui n'ont pas de prior 
		Dans test ils ont tous un prior 
		Meme min/max sur le train et le test, donc miniumun de prior est de 3 (3 commandes précèdentes)