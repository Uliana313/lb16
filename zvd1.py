import numpy as np
import matplotlib.pyplot as plt

# Оголошуємо діапазон значень x
x = np.linspace(-3, 5)

# Обчислюємо значення функції y = 2 * sin(x) + log2(|x|)
y = 2 * np.sin(x) + np.log2(np.abs(x))

# Створюємо графік
plt.plot(x, y, linestyle='--', color='purple')  # штрихова лінія (linestyle='--') і пурпуровий колір (color='purple')

# Додаємо підписи
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = 2 sin(x) + log2(|x|)')

# Зберігаємо графік у файл
plt.savefig("page.svg", format="svg")

# Показуємо графік
plt.show()
