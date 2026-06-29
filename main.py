import urllib.request
import time

def check_speed(url, iterations=10):
    print(f"Начинаем замер скорости соединения с {url}...")

    total_time = 0
    total_bytes = 0

    # Заголовки, чтобы сервер не заблокировал запросы и не отдавал кэш
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }

    for i in range(1, iterations + 1):
        req = urllib.request.Request(url, headers=headers)

        try:
            start_time = time.perf_counter()
            with urllib.request.urlopen(req) as response:
                data = response.read()
            end_time = time.perf_counter()

            # Считаем показатели текущей итерации
            elapsed_time = end_time - start_time
            data_size = len(data)

            total_time += elapsed_time
            total_bytes += data_size

            print(f"Запрос {i}/{iterations}: {elapsed_time:.3f} сек | Размер: {data_size / (1024*1024):.2f} МБ")

        except Exception as e:
            print(f"Ошибка при запросе {i}: {e}")
            continue

    if total_bytes == 0 or total_time == 0:
        print("Не удалось скачать данные.")
        return

    avg_time = total_time / iterations
    total_megabytes = total_bytes / (1024 * 1024)


    speed_mb_per_sec = total_megabytes / total_time


    speed_mbit_per_sec = speed_mb_per_sec * 8

    print("\n--- Результаты ---")
    print(f"Всего скачано данных: {total_megabytes:.2f} МБ")
    print(f"Среднее время одного запроса: {avg_time:.3f} сек")
    print(f"Скорость скачивания: {speed_mb_per_sec:.2f} МБ/с ({speed_mbit_per_sec:.2f} Мбит/с)")


if __name__ == "__main__":
    IMAGE_URL = "https://wikimedia.org" #картинка высокого разрешения
    check_speed(IMAGE_URL, iterations=10)
