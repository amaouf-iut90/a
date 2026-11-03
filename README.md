# Outils Fondamentaux - Projet de Fin de Module

Nom : MAOUF Amine
Groupe : C1

## Organisation du dépôt

Ce dépôt est organisé en deux répertoires distincts :
* TP/ : Contient mes exercices et recherches effectués pendant les séances de TP.
* projet/ : Contient mon projet personnel.

---

## Le projet : Limites de l'interpolation polynomiale

Ce projet teste l'hypothèse selon laquelle augmenter le degré d'un polynôme d'interpolation améliore systématiquement la précision de la courbe.

Pour tester cela, le programme utilise la fonction de Runge et cherche à construire un polynôme qui passe exactement par un certain nombre de ses points. La méthode utilisée repose sur la résolution de systèmes avec le Pivot de Gauss, abordée en TP.

### Comment lancer le code

1. Assurez-vous d'avoir les bibliothèques requises installées :
   ```bash
   pip install matplotlib numpy
Exécutez le script depuis la racine du projet :

Bash
python projet/tp5outils.py
Note sur l'affichage : Pour éviter que la génération du graphique ne soit bloquée par les sécurités du système d'exploitation, le script n'ouvre pas de fenêtre. Il calcule le graphique en arrière-plan et le sauvegarde directement sous forme d'image dans le fichier phenomene_runge.png.

Interprétation des résultats
L'image générée présente trois graphiques correspondant à des interpolations sur 7, 11 et 15 points. On constate que plus on ajoute de points, plus la courbe s'éloigne de la fonction initiale. Aux extrémités de l'intervalle, le tracé subit de fortes oscillations.

Ce résultat s'explique par deux facteurs.

1. Le phénomène mathématique (phénomène de Runge)
Imposer à un polynôme de degré élevé de passer par des points répartis uniformément génère des variations extrêmes sur les bords de l'intervalle. L'augmentation du nombre de points dégrade l'approximation au lieu de l'améliorer.

2. La limite informatique (précision des flottants)
Le programme construit une matrice pour résoudre le système. Le script calcule et affiche le conditionnement de cette matrice. Pour 7 points, le conditionnement reste bas. Pour 15 points, ce nombre devient extrêmement grand.

L'ordinateur stocke les nombres avec une précision limitée. Un conditionnement élevé signifie que les erreurs d'arrondi effectuées lors des calculs sont amplifiées de manière exponentielle. La courbe finale est donc faussée par l'accumulation de ces imprécisions numériques.

Conclusion :
Ce projet illustre qu'en analyse numérique, la théorie mathématique se heurte aux limites matérielles de la machine. Augmenter la complexité d'un calcul pour rechercher plus de précision peut aboutir à un résultat totalement inexploitable.

Utilisation de l'intelligence artificielle
Dans le cadre de ce projet, j'ai utilisé un assistant IA pour rédiger une partie du code et corriger des erreurs de syntaxe. J'ai cependant relu l'intégralité du code final et j'ai personnellement vérifié chaque résultat affiché pour m'assurer de la validité de l'expérience et de mes conclusions. Je l'ai aussi utilisé pour régler le problème de matplotlib bloqué sur ma machine.
