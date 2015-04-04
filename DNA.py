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

if DNK.find(Moski) and DNK.find(Belec) and DNK.find(Korencek)\
        and DNK.find(Rjave_oci) and DNK.find(Okrogel_obraz) != -1:
    print("Kradljivec je Ziga!")

elif DNK.find(Moski) and DNK.find(Belec) and DNK.find(Crni_lasje)\
        and DNK.find(Modre_oci)and DNK.find(Ovalen_obraz) != -1:
    print("Kradljivec je Matej!")

elif DNK.find(Moski)and DNK.find(Belec) and DNK.find(Rjavi_lasje)\
        and DNK.find(Zelene_oci)and DNK.find(Kvadraten_obraz) != -1:
    print("Kradljivec je Miha!")
else:
    print("OMG the thief is still on a run!")

print("Pa te imamo!")

datoteka.close()