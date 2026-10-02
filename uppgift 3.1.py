minut=int(input("hur många minuter per månad?"))
pris=int(input("hur mycket kostar det per minut?"))
if pris<300:
    pris = pris * 0.10
else:
    print(f'hej{pris:.2f}') #kallas för f-sats