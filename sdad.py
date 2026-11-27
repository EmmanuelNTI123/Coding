# undersök om en text innehåller något vitt tecken
s=input("skriv en text: ")
if " " in s or "\t" in s:
    print("innehåller vitt tecken")
else:
    print("inget vitt tecken")
# leta efter det första vita tecknet i en text

i = 0       # i används som räknare
for c in s:
    if c == " " or c == "\t":
        break
    i = i + 1
if i < len(s):
    print(f"första vita tecken finns på plats nr{i}")
else:
    print("inget vitt tecken")