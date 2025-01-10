import random
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def Decomp(tab):
    l = len(tab)
    res = tab.copy()
    while(l != 1):
        for i in range(0, l, 2):
            res[i//2] = (tab[i] + tab[i + 1])/2
            res[l -1 -i//2] = (tab[i] - tab[i + 1])/2
        #print(res)
        l = l // 2
        tab = res.copy()
    return res

def Recomp(tab):
    ltab = len(tab)
    l = 2
    res = tab.copy()
    while(l <=ltab):
        for i in range(0, l//2, 1):
            res[i*2] = tab[i] + tab[l -1 -i]
            res[i*2 + 1] = tab[i] - tab[l -1 -i]
        #print(res)
        l = l * 2
        tab = res.copy()
    return res

def RecompPart(tab,epsilon) :
    for i in range(1,len(tab),1):
        if (abs(tab[i])<epsilon):
            tab[i]=0
    return tab

def erreur(tab1,tab2):
    e=0
    for i in range (len(tab1)):
        e += (tab1[i] - tab2[i]) ** 2
    return sqrt(e)

def histoGraphe(tab, maxVal):
    decompTab = Decomp(tab.copy())
    
    plt.figure(figsize=(12, 6))  # Réduire la largeur de la figure
    
    # Graphique du tableau d'entrée
    plt.subplot(1, 3, 1)
    plt.plot(tab, marker='o')
    plt.title('Graphique du tableau d\'entrée')
    
    # Histogramme des valeurs absolues de tab regroupées par entier
    plt.subplot(1, 3, 2)
    abs_values = [abs(val) for val in decompTab]
    grouped_values = [int(val) for val in abs_values]
    plt.hist(grouped_values, bins=range(min(grouped_values), max(grouped_values) + 1))
    plt.title('Histogramme des valeurs absolues de tab regroupées par entier')
    
    # Graphique des erreurs en fonction de epsilon
    x = []
    y = []
    for i in range(0, maxVal, 1):
        epsilon = i
        recompPartTab = RecompPart(decompTab.copy(), epsilon)
        res = Recomp(recompPartTab.copy())
        e = erreur(tab, res)
        x.append(epsilon)
        y.append(e)
        
    plt.subplot(1, 3, 3)
    plt.plot(x, y)
    plt.title('Graphique des erreurs en fonction de epsilon')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    epsilon = 10
    maxVal = 100
    tab = [random.randint(0, maxVal) for _ in range(32)]
    
    # Décomposition et recomposition
    decompTab = Decomp(tab.copy())
    recompPartTab = RecompPart(decompTab.copy(),epsilon)
    res = Recomp(recompPartTab.copy())
    print("tab initial: ",tab)
    #print("tab décomposé: ",decompTab)
    #print("tab avec seuil: ",recompPartTab)
    print("tab recomposé: ",res)
    
    e = erreur(tab,res)
    print("erreur : ",e)
    
    print("\nRANDOM\n")
    histoGraphe(tab,maxVal)
    
    # Tableau de taille 32 avec les valeurs de sinus
    print("\nSINUS\n")
    tab_sin = [np.sin(2 * np.pi * i / 32)*100 for i in range(32)]
    print("tab sinus: ", tab_sin)
    histoGraphe(tab_sin, maxVal)
    
    # Tableau de taille 32 avec les valeurs de x carré
    print("\nx carré\n")
    tab_carre = [i**2 for i in range(32)]
    print("tab x carré: ", tab_carre)
    histoGraphe(tab_carre, maxVal)
    
    # Tableau de taille 32 avec les valeurs de moins x carré
    print("\nmoins x carré\n")
    tab_neg_carre = [-i**2 for i in range(32)]
    print("tab x carré: ", tab_neg_carre)
    histoGraphe(tab_neg_carre, maxVal)
    
    