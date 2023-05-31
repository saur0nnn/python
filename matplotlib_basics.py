import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
sashualo = np.mean(x)
mediana = np.median(x)
deviation = np.std(x)
print(x)
print(x + mediana)
print(x + sashualo)
print(x + deviation)

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x + mediana + 1, label='mediana')
plt.plot(x, x + sashualo, label='sashualo')
plt.plot(x, x + deviation, label='deviation')
plt.xlabel('x gerdzi')
plt.ylabel('y gerdzi')
plt.title("ra ari es")  
plt.legend()
plt.show()