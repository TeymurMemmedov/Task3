#verilən stringdə saitləri p hərfi ilə əvəz etmək
soz="proqramchinin yolu"
saitler=["a","e","i","u","o"]
for i in soz:
    if i in saitler:
        soz=soz.replace(i,"p")
print(soz)