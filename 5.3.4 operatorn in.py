# räkna blanka tecken, version 1
s=input("Skriv en text: ")
n=0
print(len(s))
for i in range(0, len(s)):
    if s[i] == " ":
        n=n+1
print(f"texten innehåller {n} blanka tecken")



# räkna blanka tecken, version 2
a=input("skriv en text: ")
e=0
for c in a:
    if c==" ":
        e=e+1
print(f"texten innehåller {e} blanka tecken")


d= "hej"
for i,c in enumerate(d):
    print(i, c)