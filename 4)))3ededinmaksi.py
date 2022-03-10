#4-cü sual - 3 ədəddən ən böyüyünü tapmaq
list = []
say = 0
while say< 3:
    eded = int(input("Ədədi daxil edin:"))
    list.append(eded)
    say += 1
print("Üç ədəddən ən böyüyü:",max(list))
