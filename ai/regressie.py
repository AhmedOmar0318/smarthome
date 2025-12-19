from dataset import genereer_dataset
import matplotlib.pyplot as plt

# --- Data ophalen ---
data = genereer_dataset()
x_vals, y_vals = zip(*data)  # makkelijker dan list comprehension

# --- Gemiddelden berekenen ---
x_mean = sum(x_vals) / len(x_vals)
y_mean = sum(y_vals) / len(y_vals)
print("Gemiddelde x:", x_mean)
print("Gemiddelde y:", y_mean)

# --- Lineaire regressie (a en b) ---
numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in data)
denominator = sum((xi - x_mean)**2 for xi, _ in data)
a = numerator / denominator
b = y_mean - a * x_mean
print("Helling (a):", a)
print("Intercept (b):", b)

# --- Visualisatie ---
plt.scatter(x_vals, y_vals, label="Data punten")
plt.plot([min(x_vals), max(x_vals)], [a*min(x_vals)+b, a*max(x_vals)+b], color='red', label="Regressielijn")
plt.xlabel("Buitentemperatuur (°C)")
plt.ylabel("Gewenste binnentemperatuur (°C)")
plt.title("Relatie tussen buiten- en gewenste binnentemperatuur")
plt.legend()
plt.show()
