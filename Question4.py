
def asal_mi(i, j=2):
    if i <= 2:
        return True if i == 2 else False
    if i % j == 0:
        return False
    if j * j > i:
        return True
    return asal_mi(i, j + 1)

def asal_sayilari_bul(baslangic, bitis):
    if baslangic > bitis:
        return
    if asal_mi(baslangic):
        print(baslangic)
    asal_sayilari_bul(baslangic + 1, bitis)

asal_sayilari_bul(500, 600)
