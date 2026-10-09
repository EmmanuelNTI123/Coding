minut=int(input("hur många minuter per månad?"))
pris_minut=int(input("hur mycket kostar det per minut?"))
pris=minut*pris_minut
if pris>300:
    pris = pris * 0.90
print(f'kostnad{pris:.2f}') #kallas för f-sats