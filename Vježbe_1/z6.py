from math import sqrt
def udaljenost_tocke(x1,y1,x2,y2,r):

 x = (x1-x2)**2 + (y1-y2)**2
 d = sqrt(x)

 if d < r:
    print(f"Točka je unutar kružnice, udaljenost je {d}")
 elif d == r:
    print(f"Točka je na kružnici, udaljenost je {d}")
 else:
    print(f"Točka je izvan kružnice, udaljenost je {d}")

udaljenost_tocke(1,2,3,4,5)

