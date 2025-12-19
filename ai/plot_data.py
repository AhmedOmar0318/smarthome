import matplotlib.pyplot as plt
from dataset import genereer_dataset

data = genereer_dataset()

x = [p[0] for p in data]
y = [p[1] for p in data]

plt.scatter(x, y)
plt.xlabel("Buitentemperatuur (°C)")
plt.ylabel("Gewenste binnentemperatuur (°C)")
plt.title("Relatie tussen buiten- en gewenste temperatuur")
plt.show()
