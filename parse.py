import os

def read_txt_files_from_directory(directory):
    """
    Зчитує вміст усіх .txt файлів у вказаній директорії та виводить кожен рядок.
    
    Args:
        directory (str): Шлях до директорії, яка містить .txt файли.
    """
    # Отримуємо список всіх файлів у директорії
    files = os.listdir(directory)

    # Фільтруємо тільки .txt файли
    txt_files = [file for file in files if file.endswith('.txt')]

    # Перебираємо кожен .txt файл і відкриваємо його для читання
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)  # Повний шлях до файлу
        with open(file_path, 'r') as file:  # Відкриваємо файл для читання
            content = file.readlines()  # Зчитуємо всі рядки у файлі
            # Виводимо кожен рядок без зайвих пробілів
            for line in content:
                print(line.strip())

# Приклад виклику функції
directory_path = 'student_marks'  # Вкажіть вашу директорію
read_txt_files_from_directory(directory_path)

