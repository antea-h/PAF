import matplotlib.pyplot as plt
import numpy as np

def jednadzba_pravca(x1,y1,x2,y2):

    nagib = (y2-y1)/(x2-x1)
    nagib = round(nagib,3)
    sl_koeficijent = -x*nagib + y
    if sl_koeficijent>0:
        sl_koeficijent = str(sl_koeficijent)
        sl_koeficijent = "+ " + sl_koeficijent
    print (f"y = {nagib}x {sl_koeficijent}")

    xpoints = np.array([x1,x2])
    ypoints = np.array([y1,y2])
    plt.scatter(x1,y1)
    plt.scatter(x2,y2)
    plt.plot(xpoints,ypoints)
    
    nacin = int(input("Unesite 1 za prikaz slike, a 2 za spremanje."))
    if nacin == 1:
        plt.show()
    if nacin == 2:
        naziv = input("Unesite naziv: ")
        plt.savefig(f"{naziv}.pdf")
        
jednadzba_pravca(15,20,11,50)
