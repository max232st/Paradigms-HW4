import numpy as np

def pearson_correlation(x, y):
    # Проверяем, что оба массива имеют одинаковую длину
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    # Вычисляем средние значения для x и y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Вычисляем числитель и знаменатель для формулы корреляции Пирсона
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator_x = np.sqrt(np.sum((x - mean_x)**2))
    denominator_y = np.sqrt(np.sum((y - mean_y)**2))

    # Вычисляем корреляцию Пирсона
    correlation = numerator / (denominator_x * denominator_y)

    return correlation

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

correlation_coefficient = pearson_correlation(array1, array2)
print("Коэффициент корреляции Пирсона:", correlation_coefficient)
