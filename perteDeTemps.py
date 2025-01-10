def Decomp(tab):
    l = len(tab)
    res = tab.copy()
    while(l != 1):
        for i in range(0, l, 2):
            res[i//2] = (tab[i] + tab[i + 1])/2
            res[l -1 -i//2] = (tab[i] - tab[i + 1])/2
        print(res)
        l = l // 2
        tab = res.copy()
    print("fin decomposition")
    return res

def Recomp(tab):
    ltab = len(tab)
    l = 2
    res = tab.copy()
    while(l <=ltab):
        for i in range(0, l//2, 1):
            res[i*2] = tab[i] + tab[l -1 -i]
            res[i*2 + 1] = tab[i] - tab[l -1 -i]
        print(res)
        l = l * 2
        tab = res.copy()
    print("fin recomposition")
    return res

if __name__ == "__main__":
    tab = [2, 7, 9, 3,1,8,2,6]
    Recomp(Decomp(tab))