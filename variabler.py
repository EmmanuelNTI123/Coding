mätarinställning=int(input("mätarinställning idag?"))
mätarinställning_för_ett_år_sedan=int(input("mätarinställning för ett år sedan?"))
antal_mil_körda=mätarinställning-mätarinställning_för_ett_år_sedan
print(antal_mil_körda)
antal_liter_bensin=int(input("antal liter"))
förbrukning_per_mil=antal_liter_bensin/antal_mil_körda
print(förbrukning_per_mil)