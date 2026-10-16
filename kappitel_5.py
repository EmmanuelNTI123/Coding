status = "godkänt" #enkel tilldelning
print(status)
halsning = "god " \
"morgon" #2. Radbrytning med backslash (\)
print(halsning)
citat = "hon sade \"hej\" till alla" #3. Citationstecken i sträng
print (citat)
sokvag = "C:\\Användare\\Dokument" #4. Escape-tecken för Backslash (\\)
print (sokvag)
meny = "Meny:\n\t1. Starta\n\t2. Avsluta" #Escape-sekvenser (\n, \t)
print (meny)
filsokvag = r"C:\ny_mapp\test.txt" #Raw Strings (r-prefix)
print (filsokvag)
pris=3
print(f'Totalt pris: {pris:.2f} kr')
intstruktion = """Välkommen! idag ska vi lära oss att programmera i Python""" #Flerradiga strängar (""")
print (intstruktion)
t4 = "Spelade \u2665 Ess"
print (t4)
print("\N{DOLLAR SIGN}")
print(chr(65))
ord = "Katt"
ord[0]
ord[-1]
len(ord)
print(ord[0])
print(ord[-1])
print(len(ord))
namn = " Emmanuel Karlsson"
print (namn[::-1])