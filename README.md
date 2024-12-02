# IA1
Notre IA repose sur un alpha-beta classique.
La profondeur de l'exploration varie selon le moment de la partie.
De 100 à 40 cases vides nous allons en profondeur 2.
De 40 à 15, profondeur 4.
De 15 à fin de partie, profondeur 8.

De plus nous avons implémenté notre propre heurisitque.
Nous cherchons à avoir les coins du plateau,
Et nous cherchons à maximiser nos mouvements possibles tout en minimisant les mouvements possibles de notre adversaire. Nous multiplions ce nombre de mouvement par 2 afin d'appuyer l'importance de cet aspect dans la recherche du meilleur coup.

Notre IA est définie dans le fichier myPlayer.py, et localGame.py nous assigne toujours les noirs.

Pour jouer, il suffit de lancer le fichier localGame.py avec python.