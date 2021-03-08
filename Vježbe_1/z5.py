from matplotlib import pyplot as plt
def jednadzba_pravca (k, l):
  return("y = {k}x + {l}")


x1 = float(input("Unesi x koordinatu prve točke: "))
y1 = float(input("Unesi y koordinatu prve točke: "))
x2 = float(input("Unesi x koordinatu druge točke: "))
y2 = float(input("Unesi y koordinatu druge točke: "))

k = (y2-y1)/(x2-x1)
l = k*x1+y1


jednadzba_pravca(k,l)


plt.plot()

plt.show()
