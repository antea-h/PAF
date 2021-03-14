import matplotlib.pyplot as plt 
import numpy as np

def jednoliko_gibanje(sila,masa):
    brzine = []
    polozaji = []
    akceleracija = sila / masa 

    vrijeme = 0
    for i in range(0,1000,1):
        brzina = akceleracija * vrijeme
        brzine.append(brzina)
        polozaj = akceleracija * (vrijeme**2) / 2
        polozaji.append(polozaj)
        vrijeme = vrijeme + 0.01

    xpoints = np.array([0,10])
    ypoints = np.array([brzine[0],brzine[-1]])
    plt.subplot(3, 1, 1)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('brzina(m/s)')
    plt.plot(xpoints,ypoints)

    ypoints = np.array([akceleracija,akceleracija])
    xpoints = np.array([0,10])
    plt.subplot(3, 1, 2)
    plt.plot(xpoints,ypoints, color = "r")
    plt.xlabel('vrijeme(s)')
    plt.ylabel('akceleracija(m/s**2)')
    plt.xlim([0,10])
    plt.ylim([0,akceleracija + 2])
    
    x_cord = np.arange(0,10,0.01)
    y_cord = [polozaji]
    plt.subplot(3, 1, 3)
    plt.scatter(x_cord,y_cord,s=1)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('polozaj(m)')
    plt.show()
    