import multiprocessing as mp
import os
import re

def search_wrapper(queue, files, keywords):
    results = {}
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            text = f.read()
        for keyword in keywords:
            if re.search(keyword, text):
                results.setdefault(keyword, []).append(file)
    queue.put(results)

def multiproces(file_path, keywords):  
    files = [file_path]
    num_processes = 4
    file_chunks = [files[i::num_processes] for i in range(num_processes)]

    queue = mp.Queue()

    processes = []
    for chunk in file_chunks:
        process = mp.Process(target=search_wrapper, args=(queue, chunk, keywords))
        process.start()
        processes.append(process)

    results = {}
    for process in processes:
        process.join()

    while not queue.empty():
        result = queue.get()
        results.update(result)

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
        multiproces(file_path, keywords)
