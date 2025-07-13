import sys
from typing import List, Dict, Optional

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Розбирає рядок логу і повертає словник із ключами: date, time, level, message.
    Якщо рядок некоректний, повертає None.
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Зчитує файл логу, парсить кожен рядок за допомогою parse_log_line.
    Повертає список словників з інформацією про кожен лог.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує список логів за рівнем level (рівень має бути в верхньому регістрі).
    """
    level_upper = level.upper()
    return list(filter(lambda log: log["level"] == level_upper, logs))

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість логів для кожного рівня.
    """
    counts = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Виводить таблицю з кількістю записів для кожного рівня логування.
    """
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print(f"{'-'*17}-|{'-'*8}")
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count:<8}")

def display_logs(logs: List[Dict[str, str]], level: str):
    """
    Виводить деталі логів для заданого рівня.
    """
    if not logs:
        print(f"Записи з рівнем '{level}' відсутні.")
        return
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу_логу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        display_logs(filtered_logs, filter_level)

if __name__ == "__main__":
    main()