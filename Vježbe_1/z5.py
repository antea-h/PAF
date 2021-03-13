import matplotlib.pyplot as plt
def jednadzba_pravca(x1,y1,x2,y2,znak):
  x_koordinate = [x1,x2]
  y_koordinate = [y1,y2]
  plt.plot(x_koordinate,y_koordinate)

  if znak == 0:
   plt.show()
  elif znak == 1:
   naziv = input("Unesite naziv slike: ")
   plt.savefig(f"{naziv}.pdf")


jednadzba_pravca(2,1,4,-2,1)





