ålder= int(input("hur gammal är du?"))

if ålder == 17:
    print("du är lika gammal som det flesta i EE25")

if ålder != 43:
    print("du är inte lika gammal som Per")
else:
    print("du är lika gammal som Per")

if ålder <= 13:
    print("du är väldigt ung")
elif ålder <18:
    print("du får inte ta körkort")
elif ålder <20:
    print("du får ta körkort")
else:
    print("du får handla på systembolaget")

namn = input("vad är ditt namn?")

if namn == "Emmanuel":
    print("kung")
elif namn == "Emanuel":
    print("så stavar man inte!")
else:
    print("varför heter du inte Emmanuel?")

if ålder == 17 and namn == "Emmanuel":
    print("du måste vara Emmanuel Karlsson")