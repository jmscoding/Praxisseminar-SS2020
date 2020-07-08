# Funktion die die Mac Adresse einer HMI ausliest

#from utils import MAC, IP


def get_mac(HMI_ADDR):
    for i in IP:
        if IP[i] == HMI_ADDR:
            HMI_NAME = i
            for j in MAC:
                if j == HMI_NAME:
                    return MAC[j]
                else:
                    continue
        else:
            continue

