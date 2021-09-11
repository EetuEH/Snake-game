
def keltainen():
    keltainen = (255, 255, 0)
    return keltainen

def musta():
    musta = (0,0,0)
    return musta

def valkoinen():
    valkoinen = (255,255,255)
    return valkoinen

#tämä metodi jäljittelee pelin vaikeustasonnostoa
def nopeus(pisteet):
    nopeus = 0
    if pisteet < 5:
        nopeus = 10
    if pisteet >=5 and pisteet < 10:
        nopeus = 15
    if pisteet >=10 and pisteet < 15:
        nopeus = 20
    if pisteet >=15 and pisteet < 20:
        nopeus = 25
    if pisteet >=20:
        nopeus = 30
    return nopeus
