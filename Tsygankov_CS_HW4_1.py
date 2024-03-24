import multiprocessing
import os
import re

def search_keywords(files, keywords, queue):
    results = {}
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
            for keyword in keywords:
                if re.search(keyword, text):
                    results.setdefault(keyword, []).append(file)
    queue.put(results)

def main():
    # Ввід шляху до файла
    file_path = input("Введіть шлях до файла: ")
    if not os.path.isfile(file_path):
        print("Файл не знайдено.")
        return

    # Ввід списка ключових слів
    keywords = input("Введіть список ключових слів через кому: ").split(",")

    files = [file_path]

    # Розділ файлів між процесами
    num_processes = 4
    file_chunks = [files[i::num_processes] for i in range(num_processes)]

    # Створення пулу процесів
    with multiprocessing.Pool(num_processes) as pool:
        queue = multiprocessing.Queue()

        # Запуск процесів
        jobs = []
        for files in file_chunks:
            jobs.append(pool.apply_async(search_keywords, args=(files, keywords, queue)))

        # Збір результатів з процесів
        results = {}
        for job in jobs:
            results.update(job.get())

        # Виведення результатів
        for keyword, files in results.items():
            print(f"Keyword: {keyword}")
            for file in files:
                print(f"\t{file}")

if __name__ == '__main__':
    main()


