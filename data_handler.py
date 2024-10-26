import os

# Вказуємо директорію з .txt файлами
directory = 'student_marks'

# Отримуємо всі .txt файли, окрім students.txt (файл з іменами)
files = [file for file in os.listdir(directory) if file.endswith('.txt') and file != 'student_names.txt']

# Читаємо імена студентів з файлу student_names.txt
with open(os.path.join(directory, 'student_names.txt'), 'r') as f:
    student_names = [line.strip() for line in f.readlines()]

# Створюємо словник для оцінок за предметами
subject_marks = {file.replace('.txt', ''): [] for file in files}

# Зчитуємо оцінки з кожного файлу та зберігаємо їх у словнику
for txt_file in files:
    subject_name = txt_file.replace('.txt', '')  # Назва предмета з імені файлу
    file_path = os.path.join(directory, txt_file)  # Повний шлях до файлу
    with open(file_path, 'r') as file:  # Відкриваємо файл для читання
        marks = [int(line.strip()) for line in file.readlines()]  # Зчитуємо оцінки як числа
        subject_marks[subject_name].extend(marks)  # Додаємо оцінки до відповідного предмета

# Перевіряємо, чи кількість студентів відповідає кількості оцінок у кожному предметі
for subject, marks in subject_marks.items():
    if len(marks) != len(student_names):
        raise ValueError(f"Кількість оцінок у {subject} не відповідає кількості студентів.")

# Створюємо словник, що містить оцінки для кожного студента за всі предмети
student_data = {
    student: {subject: subject_marks[subject][i] for subject in subject_marks}
    for i, student in enumerate(student_names)
}

# Виводимо результати у потрібному форматі
for student, subjects in student_data.items():
    print(f"Ім'я студента: {student}")
    print("Оцінки з предметів:")
    total_marks = 0

    for subject, mark in subjects.items():
        print(f"{subject}: {mark}")
        total_marks += mark

# Обчислюємо середнє значення оцінок
    average = total_marks / len(subjects)
    print(f"Середнє значення оцінок: {average:.2f}")  # Виводимо середнє з двома знаками після коми
    print("-" * 30)  # Роздільник між студентами
