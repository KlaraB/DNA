datoteka = open("DNK.txt", "r")
DNK = datoteka.read()

Crni_lasje = "CCAGCAATCGC"
Rjavi_lasje = "GCCAGTGCCG"
Korencek = "TTAGCTATCGC"

Kvadraten_obraz = "GCCACGG"
Okrogel_obraz = "ACCACAA"
Ovalen_obraz = "AGGCCTCA"

Modre_oci = "TTGTGGTGGC"
Zelene_oci = "GGGAGGTGGC"
Rjave_oci = "AAGTAGTGAC"

Moski = "TGCAGGAACTTC"
Zenska = "TGAAGGACCTTC"

Belec = "AAAACCTCA"
Crnec = "CGACTACAG"
Azijec = "CGCGGGCCG"

if DNK.count(Moski) and DNK.count(Belec) and DNK.count(Korencek)\
        and DNK.count(Rjave_oci) and DNK.count(Okrogel_obraz) == 1:
    print("Kradljivec je Ziga!")

elif DNK.count(Moski) and DNK.count(Belec) and DNK.count(Crni_lasje)\
        and DNK.count(Modre_oci)and DNK.count(Ovalen_obraz) == 1:
    print("Kradljivec je Matej!")

elif DNK.count(Moski)and DNK.count(Belec) and DNK.count(Rjavi_lasje)\
        and DNK.count(Zelene_oci)and DNK.count(Kvadraten_obraz) == 1:
    print("Kradljivec je Miha!")
else:
    print("OMG the thief is still on a run!")

print("Pa te imamo!")

datoteka.close()