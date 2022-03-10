#Üçüncü sual-Daxil edilən ədədlərin rəqəmləri cəmini tapmaq
limit=int(input("Neçə ədədin rəqəmləri cəmini tapmaq istəyirsiniz?: "))
say=0
while say<limit:
    cem=0
    eded=int(input("Ədədi daxil edin:"))
    eded=str(eded)
    for i in eded:
        i=int(i)
        cem+=i
    say+=1
    print(say,"-ci ədədin rəqəmləri cəmi",cem)