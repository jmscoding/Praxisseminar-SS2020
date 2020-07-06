# Funktion die die Mac Adresse einer HMI ausliest

from utils import MAC, IP
from hmi import HMI_ADDR

def get_mac():
    for i in IP:
        if i.values() == HMI_ADDR:
            HMI_NAME = i.keys()
            for j in MAC:
                if j.values() == HMI_NAME:
                    return j.keys()
                else:
                    continue
        else:
            continue
