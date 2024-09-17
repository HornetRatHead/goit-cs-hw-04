import threading
import os
import re

def search_keywords(files, keywords):
    results = {}
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            text = f.read()
        for keyword in keywords:
            if re.search(keyword, text):
                results.setdefault(keyword, []).append(file)
    return results

def thread(file_path, keywords):  # Зміна: приймає аргументи
    files = [file_path]
    num_threads = 4
    file_chunks = [files[i::num_threads] for i in range(num_threads)]

    threads = []
    results = {}

    def search_wrapper(files, keywords):
        nonlocal results
        results.update(search_keywords(files, keywords))

    for chunk in file_chunks:
        thread = threading.Thread(target=search_wrapper, args=(chunk, keywords))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for keyword, files in results.items():
        print(f"Keyword: {keyword}")
        for file in files:
            print(f"\t{file}")


if __name__ == '__main__':
    # Шляху до файлу та ключових слів
    file_path = input("Введіть шлях до файлу: ")
    if not os.path.isfile(file_path):
        print("Файл не знайдено.")
    else:
        keywords = input("Введіть список ключових слів через кому: ").split(",")
        # Виклик функції thread з введеними значеннями
        thread(file_path, keywords)
