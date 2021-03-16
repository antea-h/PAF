from math import sqrt
import matplotlib.pyplot as plt
def udaljenost_tocke(x1,y1,x2,y2,r):

  kruznica = plt.Circle((x2,y2),r,color = "r")
  tocka = plt.Circle((x1,y1),0.2, color = "black")
    fig, ax = plt.subplots()
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])
    ax.add_patch(kruznica)
    ax.add_patch(tocka)
   plt.plot(x1,y1,"bo")

  x = (x1-x2)**2 + (y1-y2)**2
  d = sqrt(x)

 epsilon = 0.01
 if d < r:
    print(f"Točka je unutar kružnice, udaljenost je {d}")
 elif r-epsilon < d < r+epsilon:
    print(f"Točka je na kružnici, udaljenost je {d}")
 else:
    print(f"Točka je izvan kružnice, udaljenost je {d}")

 nacin = int(input("Unesite 1 za prikaz slike, a 2 za spremanje."))
 if nacin == 1:
    plt.show()
 elif nacin == 2:
    naziv = input("Unesite naziv slike: ")
    plt.savefig(f"{naziv}.pdf")


udaljenost_tocke(1,2,3,4,5)

