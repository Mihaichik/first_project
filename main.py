import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env в систему
load_dotenv()

def print_author():
    # Читаем переменную AUTHOR из окружения
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

# Этот блок запустит функцию при старте файла
if __name__ == "__main__":
    print_author()
