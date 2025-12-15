from api import forecast_7d

def genereer_dataset(n=50):
    data = []
    for _ in range(n):
        buiten_temp = forecast_7d()
        if buiten_temp is None:
            continue

        # Simuleer gewenste binnentemp (target)
        desired_temp = 20 + (15 - buiten_temp) * 0.3

        data.append((buiten_temp, desired_temp))
    return data

if __name__ == "__main__":
    dataset = genereer_dataset()
    for i, (x, y) in enumerate(dataset[:10], 1):
        print(f"{i:02d}: buiten={x:.2f}°C -> desired={y:.2f}°C")
