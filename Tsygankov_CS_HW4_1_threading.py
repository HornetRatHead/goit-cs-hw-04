
import threading
import os
import re

def search_keywords(files, keywords):

    results = {}
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:  # Відкриття з визначенням кодування
            text = f.read()
            for keyword in keywords:
                if re.search(keyword, text):
                    results.setdefault(keyword, []).append(file)
    return results  # Повернення результатів

def main():
    """
    Функція для пошуку ключових слів у файлах з використанням потоків.
    """
    # Ввід шляху до файла
    file_path = input("Введіть шлях до файла: ")
    if not os.path.isfile(file_path):
        print("Файл не знайдено.")
        return

    # Ввід списка ключових слів
    keywords = input("Введіть список ключових слів через кому: ").split(",")

    files = [file_path]

    # Розділ файлів між потоками
    num_threads = 4
    file_chunks = [files[i::num_threads] for i in range(num_threads)]

    # Створення та запуск потоків
    threads = []
    for files in file_chunks:
        def search_wrapper(files, keywords):
            results = search_keywords(files, keywords)
            local_result = results
            return local_result

    # Збір результатів з потоків
    results = {}
    for thread in threads:
        thread.join()
        if thread.result is not None:
            results.update(thread.result) # Оновлення словника results

    # Виведення результатів
    for keyword, files in results.items():
        print(f"Keyword: {keyword}")
        for file in files:
            print(f"\t{file}")

if __name__ == '__main__':
    main()


