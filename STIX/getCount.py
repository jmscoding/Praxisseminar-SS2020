# Funktion die abprüft wie oft das Elementenpaar in der Liste vorkommt


def getCount(e1, e2, liste):
    c = 0
    for e in liste:
        if e1 == e[3] and e2 in e[2]:
            c += 1
    return c
