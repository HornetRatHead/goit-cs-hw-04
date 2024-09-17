import time
import os
from Tsygankov_CS_HW4_1_multiprocessing import multiproces
from Tsygankov_CS_HW4_1_threading import thread

def run_and_measure_time(function, file_path, keywords):
    """
    Запускає функцію (або multiproces, або thread) та вимірює час її виконання.
    """
    start_time = time.time()
    function(file_path, keywords)  # Викликаємо функцію напряму
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def main():
    file_path = input("Введіть шлях до файлу: ")
    if not os.path.isfile(file_path):
        print("Файл не знайдено.")
        return

    keywords = input("Введіть список ключових слів через кому: ").split(",")

    # Запуск функцій і вимірювання часу
    print(f"Запуск multiprocessing скрипту")
    time1 = run_and_measure_time(multiproces, file_path, keywords)
    print(f"Час виконання multiprocessing: {time1:.2f} секунд")

    print(f"\nЗапуск threading скрипту")
    time2 = run_and_measure_time(thread, file_path, keywords)
    print(f"Час виконання threading: {time2:.2f} секунд")

    # Порівняння часу
    if time1 < time2:
        print(f"\nMultiprocessing виконується швидше ніж threading.")
    elif time1 > time2:
        print(f"\nThreading виконується швидше ніж multiprocessing.")
    else:
        print(f"\nОбидві функції виконані за однаковий час.")

if __name__ == '__main__':
    main()