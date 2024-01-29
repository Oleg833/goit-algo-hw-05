import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def measure_time(algorithm, text, pattern, number=1000):
    return timeit.timeit(lambda: algorithm(text, pattern), number=number)

# Зчитуємо дані з файлів
with open('text1.txt', 'r', encoding='utf-8') as file1:
    text1 = file1.read()

with open('text2.txt', 'r', encoding='utf-8') as file2:
    text2 = file2.read()

# Генеруємо підрядки
existing_pattern = "UA5.ORG [Електронний ресурс]"
existing_pattern2 = "AMD Ryzen 5 3600"
fake_pattern = "your_fake_pattern"

algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]

for algorithm in algorithms:
    print(f"\nTesting algorithm: {algorithm.__name__}")
    
    # Вимірюємо час для реального підрядка
    time_existing = measure_time(algorithm, text1, existing_pattern)
    print(f"Час для реального підрядка в тексті 1: {time_existing} сек")

    # Вимірюємо час для вигаданого підрядка
    time_fake = measure_time(algorithm, text1, fake_pattern)
    print(f"Час для вигаданого підрядка в тексті 1: {time_fake} сек")

    # Повторюємо те саме для тексту 2
    time_existing2 = measure_time(algorithm, text2, existing_pattern2)
    print(f"Час для реального підрядка в тексті 2: {time_existing2} сек")

    time_fake2 = measure_time(algorithm, text2, fake_pattern)
    print(f"Час для вигаданого підрядка в тексті 2: {time_fake2} сек")
