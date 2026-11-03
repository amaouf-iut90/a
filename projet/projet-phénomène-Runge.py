import matplotlib
matplotlib.use('Agg') 

import matplotlib.pyplot as plt
import numpy as np



def resoudre(A, b):
    """Résolution de système linéaire par pivot de Gauss partiel."""
    n = len(A)
    M = [ligne[:] for ligne in A]
    v = list(b)
    
    for i in range(n):
        ligne_pivot = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[ligne_pivot][i]):
                ligne_pivot = k
                
        M[i], M[ligne_pivot] = M[ligne_pivot], M[i]
        v[i], v[ligne_pivot] = v[ligne_pivot], v[i]
        
        for j in range(i + 1, n):
            facteur = M[j][i] / M[i][i]
            for k in range(i, n):
                M[j][k] -= facteur * M[i][k]
            v[j] -= facteur * v[i]
            
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (v[i] - somme) / M[i][i]
        
    return x

def evaluer_polynome(coefs, x):
    """Évaluation d'un polynôme par la méthode de Horner."""
    resultat = 0
    for c in reversed(coefs):
        resultat = resultat * x + c
    return resultat

def creer_vandermonde(xs):
    """Crée la matrice de Vandermonde associée aux abscisses xs."""
    n = len(xs)
    return [[x**j for j in range(n)] for x in xs]



def fonction_runge(x):
    """La fonction piège par excellence pour l'interpolation."""
    return 1 / (1 + 25 * x**2)

# On va tester avec 7, 11 et 15 points
nb_points_tests = [7, 11, 15]

plt.figure(figsize=(15, 5))
xs_continus = np.linspace(-1, 1, 500) # Pour tracer les courbes lisses

for index, n in enumerate(nb_points_tests):
    # 1. Générer n points répartis uniformément entre -1 et 1
    xs_echantillon = [ -1 + 2 * i / (n - 1) for i in range(n) ]
    ys_echantillon = [ fonction_runge(x) for x in xs_echantillon ]
    
    # 2. Créer le système V * C = Y
    V = creer_vandermonde(xs_echantillon)
    
    # 3. Résoudre le système pour trouver les coefficients du polynôme
    coefficients = resoudre(V, ys_echantillon)
    
    # Calcul du conditionnement (pour l'analyse critique dans le README)
    conditionnement = np.linalg.cond(V)
    
    # 4. Préparer le tracé du polynôme trouvé
    ys_polynome = [evaluer_polynome(coefficients, x) for x in xs_continus]
    ys_vrais = [fonction_runge(x) for x in xs_continus]
    
    # 5. Affichage
    plt.subplot(1, 3, index + 1)
    plt.plot(xs_continus, ys_vrais, 'k--', label="Fonction de Runge")
    plt.plot(xs_continus, ys_polynome, 'r-', label=f"Polynôme (degré {n-1})")
    plt.plot(xs_echantillon, ys_echantillon, 'bo', label="Points d'interpolation")
    
    plt.ylim(-0.5, 2)
    plt.title(f"{n} points\nCond(V) = {conditionnement:.1e}")
    plt.legend()

plt.suptitle("Le désastre de l'interpolation polynomiale (Phénomène de Runge)")
plt.tight_layout()

# SAUVEGARDE DE L'IMAGE Remplace plt.show() pour éviter le blocage
nom_fichier = "phenomene_runge.png"
plt.savefig(nom_fichier, dpi=300)
print(f"Succès ! L'image a été sauvegardée sous le nom : {nom_fichier}")
