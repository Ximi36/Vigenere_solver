#Funkcja szukajaca par liczb, ktorych NWW jest rowna dlugosci wprowadzoengo ciagu
def szukaj_par_nww(dlugoscKlucza):
    dzielnikiDlugosciKlucza = []
    for i in range(1, dlugoscKlucza + 1):
        if dlugoscKlucza % i == 0:
            dzielnikiDlugosciKlucza.append(i)
    paryNWW = []

    for i in range(len(dzielnikiDlugosciKlucza)):
        for j in range(i, len(dzielnikiDlugosciKlucza)):
            if dzielnikiDlugosciKlucza[i] * dzielnikiDlugosciKlucza[j] % dlugoscKlucza == 0 and dzielnikiDlugosciKlucza[i] != 1 and dzielnikiDlugosciKlucza[j] != 1:
                paryNWW.append((dzielnikiDlugosciKlucza[i], dzielnikiDlugosciKlucza[j]))
    return paryNWW

#Funkcja zmieniajaca znaki z jezyka polskiego na ich standardowe odpowiedniki
def polskie_na_standardowe(word):
    translation_table = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    return ''.join([translation_table.get(litera, litera) for litera in word])

#Funkcja pomocnicza do roszczerzania dlugosci slowa by odpowiadala ona dlugosci wprowadzonego klucza (latwo sie dodawalo)
def standaryzacja_dlugosci_slowa(word, dlugoscKlucza):
    n = dlugoscKlucza // len(word)
    reszta = dlugoscKlucza % len(word)
    return word * n + word[:reszta]


'''
#Funkcja kodujaca vigenerem z podanym kluczem
def kodowanie_vigenere(tekstJawny, klucz):
    zakodowanyTekst = ''
    for i in range(len(tekstJawny)):
        literaJawnego = tekstJawny[i]
        literaKlucza = klucz[i % len(klucz)]
        przesuniecie = ord(literaKlucza.lower()) - ord('a')
        if literaJawnego.isalpha() or literaJawnego == "{":
            literaJawnego = literaJawnego.lower()
            zakodowanyTekst += chr((ord(literaJawnego) - ord('a') + przesuniecie) % 26 + ord('a'))
        else:
            zakodowanyTekst += literaJawnego
    return zakodowanyTekst
'''


#Funkcja kodujaca vigenerem z podanym kluczem dla alfabetu ze spacja na koncu
def kodowanie_vigenere(tekstJawny, klucz):
    zakodowanyTekst = ''
    for i in range(len(tekstJawny)):
        literaJawnego = tekstJawny[i]
        literaKlucza = klucz[i % len(klucz)]
        przesuniecie = ord(literaKlucza.lower()) - ord('a')
        if literaJawnego.isalpha() or literaJawnego == "{":
            literaJawnego = literaJawnego.lower()
            zakodowanyTekst += chr((ord(literaJawnego) - ord('a') + przesuniecie) % 27 + ord('a'))
        else:
            zakodowanyTekst += literaJawnego
    return zakodowanyTekst




#Funkcja do ladowania slownika, linia po linii
def zaladuj_slownik(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def main():
    polish_words = zaladuj_slownik("rzeczownikilepsze.txt")
    standardoweSlowa = [polskie_na_standardowe(word) for word in polish_words]

    klucz = input("Podaj ciąg znaków: ")
    dlugoscKlucza = len(klucz)
    print("Długość podanego ciągu:", dlugoscKlucza)

    paryNWW = szukaj_par_nww(dlugoscKlucza)
    print("Możliwe pary składników dające NWW równą długości ciągu:")
    for paraNWW in paryNWW:
        print(paraNWW)

    for paraNWW in paryNWW:
        pierwszeSlowa = [standaryzacja_dlugosci_slowa(word, dlugoscKlucza) for word in standardoweSlowa if len(word) == paraNWW[0]]
        drugieSlowa = [standaryzacja_dlugosci_slowa(word, dlugoscKlucza) for word in standardoweSlowa if len(word) == paraNWW[1]]

        print("Szukanie dla ", paraNWW)

        znalezionoDopasowanie = False
        for pierwszeSlowo in pierwszeSlowa:
            pierwszeSlowo = polskie_na_standardowe(pierwszeSlowo)
            for drugieSlowo in drugieSlowa:
                drugieSlowo = polskie_na_standardowe(drugieSlowo)
                zakodowanyTekst = kodowanie_vigenere(pierwszeSlowo, drugieSlowo)
                if zakodowanyTekst == klucz.lower():
                    znalezionoDopasowanie = True
                    print("Znaleziono:", pierwszeSlowo, "+", drugieSlowo, "=", zakodowanyTekst)
                    break
            if znalezionoDopasowanie:
                break
        if znalezionoDopasowanie:
            break


if __name__ == "__main__":
    main()
