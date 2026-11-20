# undersök om en text innehåller något vitt tecken
s=input("skriv en text: ")
if " " in s or "\t" in s:
    print("innehåller vitt tecken")
else:
    print("inget vitt tecken")