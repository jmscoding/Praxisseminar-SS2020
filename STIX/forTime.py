

def getMon(mon):
    try:
        if 'Jan' in mon:
            return '01'
        elif 'Feb' in mon:
            return '02'
        elif 'Mar' in mon:
            return '03'
        elif 'Apr' in mon:
            return '04'
        elif 'May' in mon:
            return '05'
        elif 'Jun' in mon:
            return '06'
        elif 'Jul' in mon:
            return '07'
        elif 'Aug' in mon:
            return '08'
        elif 'Sep' in mon:
            return '09'
        elif 'Okt' in mon:
            return '10'
        elif 'Nov' in mon:
            return '11'
        elif 'Dez' in mon:
            return '12'
    except NameError:
        print(mon + ' ist nicht definiert!')


def fortime(zeit):
    year = zeit[8:12]
    month = getMon(str(zeit[0:9]))
    day = zeit[4:6]
    std = str(int(zeit[13:15]) - 2)
    m = zeit[16:18]
    sec = zeit[19:25]

    s = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(std) + ":" + str(m) + ":" + str(sec) + "Z"

    return s
