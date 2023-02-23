#Liste mit Barcodes

Liste_Zeichenkette_Strichcode = []

#Eingabe Barcode

Barcode_Eingabe = str(input("Geben sie den Barcode ein!"))

if Barcode_Eingabe.isalpha():

    print("Fehlercode 1 = String enthält nicht ausschließlich Ziffern")

elif Barcode_Eingabe.isdigit():

    print("Die Eingabe ist korrekt und besteht nur aus Ziffern")
    Liste_Zeichenkette_Strichcode.append(Barcode_Eingabe)
    print("Der Barcode wurde der Liste hinzugefügt")

for s_8 in Liste_Zeichenkette_Strichcode:

    Nettogewicht = int(s_8[9:14])
    Bruttogewicht = int(s_8[19:24])

    if (Bruttogewicht < Nettogewicht):

        print("Fehlercode 2 = Nettogewicht ist größer als Bruttogewicht")

