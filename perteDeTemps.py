import random
from math import sqrt
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
    
    # histogramme des valeurs absolues de tab
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist([abs(val) for val in decompTab], bins=100)
    plt.title('Histogramme des valeurs absolues de tab')
    
    # graphique des erreurs en fonction de epsilon
    x = []
    y = []
    for i in range(0, maxVal, 1):
        epsilon = i
        recompPartTab = RecompPart(decompTab.copy(),epsilon)
        res = Recomp(recompPartTab.copy())
        e = erreur(tab,res)
        x.append(epsilon)
        y.append(e)
        
    plt.subplot(1, 2, 2)
    plt.plot(x, y)
    plt.title('Graphique des erreurs en fonction de epsilon')
    plt.tight_layout()
    plt.show()
    
    