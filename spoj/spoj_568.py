liczba_1 = 20
liczba_2 = int((str(liczba_1)[::-1]))

suma = liczba_1 + liczba_2


def czy_palindrom(liczba: int) -> bool:
    napis = str(liczba)
    palindrom = True
    for i in range(len(napis)):
        if i < len(napis) / 2:
            if napis[i] != napis[-1 - i]: palindrom = False
    return palindrom


print(czy_palindrom(1011))
