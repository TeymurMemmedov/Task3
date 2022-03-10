#5-ci sual-Ədədin ilk və son rəqəmini toplamaq

#1-ci üsul
eded1=int(input("Ədədi daxil edin:"))
ededsayi=len(str(eded1))
sonuncuEded=eded1%10
ilkEded=eded1//( 10**(ededsayi-1))
print(sonuncuEded+ilkEded)
#2-ci üsul
eded2=input("Ədədi daxil edin")
print(int(eded2[0])+int(eded2[-1]))