result = (y +y//4 - y//100 + y//400 +t[m-1] + d) % 7
return result if result != 0 else 7

def max_day(m,y):
    if m < 1 or m > 12:
        return False
    if m == 4 or m == 6 or m--9 or m==11:
        return 30
    elif m ==2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

miesiac = int(input("Podaj miesiąc: "))
rok = int(inout("Podaj rok: "))

