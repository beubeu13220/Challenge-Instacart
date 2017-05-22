# Challenge-Instacart

## Remarque :

*N°1 :* 
Par rapport à la table order, la distribution sur les variables de order sont les mêmes pour le train et le test 

*N°2 :* 
Observer si les commandes réalisée dans un délai plus court que habituellement, ou si la commande a lieu un jour inabituel si il y'a des reoder.
En effet commander un jours après une prècédente commande peut concerner un oublie 

*N°3 :* 
Order_products_train ne contient que des commandes des commande id qui ont un eval_set à "train"

*N°4 :* 
si j'achete deux fois le même produit et que j'en recommande un ?
comment cela se passe ? 
On confirme qu'il ny'a pas de reordered lors de la première commande 

## Stats descriptive potentiellement intérressant 

1. Le nombre de produit commandé par commande
2. Le nombre de reoder par commande 
3. Nombre produit/ nombre reoder selon le jour l'heure et l'espacement avec précédente commande
4. Le type de produit reoder 
5. le taux de reordered
6. le type de produit reoder selon le jour l'heure et l'espacement avec précédente commande

faire ses stats avec le merge du train et du prior  
faire ses stats que sur le prior

faire des stats sur le lien entre le train et le order 


## Idée d'approche numéro 1 :

	- Créer des clusters de produit, selon leur caractéristique et si ils sont commandé ensemble
	- Ensuite prédire la commande ou non de ces clusters
	- Faire différents datasets avec les order numbers (un dataset avec les 3 dernières commandes, 4, 5, 6?)
	- regarder les produits toujours re commandé ou jamais recommande une fois commandé
	- regarder si il y'a des ID dans le test qui n'ont pas de prior 
		Dans test ils ont tous un prior 
		Meme min/max sur le train et le test, donc miniumun de prior est de 3 (3 commandes précèdentes)

## Idée d'approche numéro 2 :

	- On crée des mesure de similarité entre produits et users
		- Word2vec (pckg : gensim)
		- Factorisation de matrice (cf netflix)
		- LDA
		- PLSA
		- Dot product 
		- Koren SVD
		- RNN 
	- On utilise ANNOY indexe pour récupérer les K-plus proches produits (pckg: Annoy)
	- On utilse un modèle pour mettre des poids à chaque source, puis rank les produits, en supervisant avec le train

	- Question : Comment trouver le K? en supervisant sur le train ?



## Resources :

1. [From Word Embeddings to Item Recommendation, *Makbule Gulcin Ozsoy*](https://arxiv.org/pdf/1601.01356.pdf)
2. [Distributed Representations of Sentences and Documents, *Quoc Lee et al.*](https://cs.stanford.edu/~quocle/paragraph_vector.pdf)
3. [ITEM2VEC: NEURAL ITEM EMBEDDING FOR COLLABORATIVE FILTERING , *Oren Barkan et al.*](https://arxiv.org/pdf/1603.04259.pdf)
4. [Machine Learning & Big data @ Spotify, *Andy Sloane*](https://www.a1k0n.net/spotify/ml-madison/#/33)
5. [Similarity Queries using Annoy Tutorial](https://markroxor.github.io/gensim/static/notebooks/annoytutorial.html)
6. [Nearest neighbor methods and vector models – part 1, *Erik Bernhardsson* ](https://erikbern.com/2015/09/24/nearest-neighbor-methods-vector-models-part-1.html)
7. [Music recommendations mlconf, *Erik Bernhardsson* ](https://www.slideshare.net/erikbern/music-recommendations-mlconf-2014)
8. [Model benchmarks, *Erik Bernhardsson* ](https://erikbern.com/2013/11/02/model-benchmarks/)

