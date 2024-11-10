import matplotlib.pyplot as plt

# Зчитування даних із текстового файлу
data = {}
with open("cars.txt", "r") as file:
    for line in file:
        # Розділяємо кожен рядок на ключ і значення
        car, price = line.strip().split(":")
        data[car.strip()] = int(price.strip())

# Підготовка даних для побудови гістограми
cars = list(data.keys())
prices = list(data.values())

# Побудова горизонтальної гістограми з налаштуванням відображення
plt.figure(figsize=(10, 6))  # Змінює розмір графіка
plt.barh(cars, prices, color="skyblue")
plt.xlabel("Ціна", fontsize=12)
plt.ylabel("Марка автомобіля", fontsize=12)
plt.title("Ціни на автомобілі", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Відображення гістограми
plt.show()

