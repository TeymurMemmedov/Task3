#Birinci sual-Stringdə hər hərf neçe dəfə işlənib?
soz=input("Sözü daxil edin:")
luget={herf:soz.count(herf) for herf in soz}
print(luget)