a = int(input())
b = int(input())
c = int(input())

if (a<=0 or b<=0 or c<=0):
    print("Ошибка: стороны треугольника могут быть только натуральными числами")

else:
    if (max(a,b,c) >= (a+b+c-max(a,b,c))):
        print("Треугольника с такими сторонами не существует")
    else:
        maxx = max(a,b,c)
        if (maxx == a):
            a = c
            c = maxx
        elif (maxx == b):
            b = c
            c = maxx

        if (c*c < (a*a + b*b)):
            print("Треугольник остроугольный")
        elif (c*c == (a*a + b*b)):
            print("Треугольник прямоугольный")
        else:
            print("Треугольник тупоугольный")
        
