a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("Üç sayı birbirine eşittir")
elif a>b:
    if a>c:
        print("En büyük sayı:",a)
    else:
        print("En büyük sayı:",c)
else:
    if b>c:
        print("En büyük sayı:",b)
    else:
        print("En büyük sayı:",c)