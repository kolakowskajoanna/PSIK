#zadanie 1
tekscior="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
         "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później " \
         "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w " \
         "latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z " \
         "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach " \
         "osobistych, jak Aldus PageMaker"
print(tekscior)
#zadanie 2
imie="joanna"
nazwisko="kolakowska"
pierwsza_litera=tekscior.count(imie[1])
druga_litera=tekscior.count(nazwisko[2])

print("W tekscie jest ",pierwsza_litera," liter 'o' i ",druga_litera," liter 'l'")
