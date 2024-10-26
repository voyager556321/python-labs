import os

# Вказуємо директорію з .txt файлами
directory = 'student_marks'

# Отримуємо всі .txt файли, окрім student_names.txt (файл з іменами)
files = [file for file in os.listdir(directory) if file.endswith('.txt') and file != 'student_names.txt']

# Читаємо імена студентів з файлу student_names.txt
with open(os.path.join(directory, 'student_names.txt'), 'r') as f:
    student_names = [line.strip() for line in f.readlines()]

# Створюємо словник для оцінок за предметами
subject_marks = {file.replace('.txt', ''): [] for file in files}

# Зчитуємо оцінки з кожного файлу та зберігаємо їх у словнику
for txt_file in files:
    subject_name = txt_file.replace('.txt', '')  
    file_path = os.path.join(directory, txt_file)  
    with open(file_path, 'r') as file:  
        marks = [int(line.strip()) for line in file.readlines()]  
        subject_marks[subject_name].extend(marks)  

# Перевіряємо, чи кількість студентів відповідає кількості оцінок
for subject, marks in subject_marks.items():
    if len(marks) != len(student_names):
        raise ValueError(f"Кількість оцінок у {subject} не відповідає кількості студентів.")

# Створюємо словник для зберігання даних студентів
student_data = {
    student: {subject: subject_marks[subject][i] for subject in subject_marks}
    for i, student in enumerate(student_names)
}

# Виведення середніх оцінок студентів та формування списку
average_scores = {}
for student, subjects in student_data.items():
    total_marks = sum(subjects.values())
    average = total_marks / len(subjects)
    average_scores[student] = average
    print(f"Студент: {student}, середня оцінка: {average:.2f}")

print("\nТоп-3 студенти за середніми оцінками:")
top_students = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (student, avg) in enumerate(top_students, start=1):
    print(f"{i}. {student} з середньою оцінкою: {avg:.2f}")

print(f"\nЗагальна кількість студентів: {len(student_names)}")

# Обчислення середньої, мінімальної та максимальної оцінки по кожному предмету
for subject, marks in subject_marks.items():
    avg = sum(marks) / len(marks)
    min_mark = min(marks)
    max_mark = max(marks)
    print(f"\nПредмет: {subject}, середня оцінка: {avg:.2f}, min оцінка: {min_mark}, max оцінка: {max_mark}")

    # Знаходження студента з найвищою оцінкою
    max_student = student_names[marks.index(max_mark)]
    print(f"Предмет: {subject} | Студент: {max_student}, оцінка: {max_mark}")

# Знаходження студентів із середньою оцінкою нижче 50
low_score_students = [student for student, avg in average_scores.items() if avg < 50]
print(f"\nКількість студентів з середньою оцінкою нижче 50: {len(low_score_students)}")
for student in low_score_students:
    print(student)

