from api import forecast_7d

def genereer_dataset():
    data = []

    max_temps, min_temps = forecast_7d()

    for buiten_temp in max_temps:
        # simpele target: kouder buiten → warmer binnen
        desired_temp = 20 + (15 - buiten_temp) * 0.3
        data.append((buiten_temp, desired_temp))

    return data


if __name__ == "__main__":
    dataset = genereer_dataset()
    for i, (x, y) in enumerate(dataset, 1):
        print(f"{i}: buiten={x:.2f}°C -> gewenst={y:.2f}°C")
