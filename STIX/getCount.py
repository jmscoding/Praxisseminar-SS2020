# Funktion die abprüft wie oft das Elementenpaar in der Liste vorkommt


def getCount(e3, e1, e2, liste):
    c = 0
    for e in liste:
        if e1 in e[3] and e2 in e[2] and e3 in e[1]:
            c += 1
    return c
