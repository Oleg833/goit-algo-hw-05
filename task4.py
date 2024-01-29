import timeit
from boyer_moore_search import boyer_moore_search

# Зчитуємо дані з файлів
with open('text1.txt', 'r', encoding='utf-8') as file1:
    text1 = file1.read()

with open('text2.txt', 'r', encoding='utf-8') as file2:
    text2 = file2.read()

# Генеруємо підрядки
existing_pattern = "БІБЛІОТЕКАХ"
fake_pattern = "your_fake_pattern"

# Вимірюємо час для реального підрядка
time_existing = timeit.timeit(lambda: boyer_moore_search(text1, existing_pattern), number=10)

# Вимірюємо час для вигаданого підрядка
time_fake = timeit.timeit(lambda: boyer_moore_search(text1, fake_pattern), number=10)

print(f"Час для реального підрядка: {time_existing} сек")
print(f"Час для вигаданого підрядка: {time_fake} сек")



def measure_time(algorithm, text, pattern, number=10):
    return timeit.timeit(lambda: algorithm(text, pattern), number=number)


# Вимірюємо час для реального підрядка
time_existing = measure_time(boyer_moore_search, text1, existing_pattern)

# Вимірюємо час для вигаданого підрядка
time_fake = measure_time(boyer_moore_search, text1, fake_pattern)

print(f"1Час для реального підрядка: {time_existing} сек")
print(f"1Час для вигаданого підрядка: {time_fake} сек")

