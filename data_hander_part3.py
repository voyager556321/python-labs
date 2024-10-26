import os

def get_files(directory):
    """Отримує всі .txt файли, окрім student_names.txt."""
    return [file for file in os.listdir(directory) if file.endswith('.txt') and file != 'student_names.txt']

def read_student_names(directory):
    """Читає імена студентів з файлу student_names.txt."""
    with open(os.path.join(directory, 'student_names.txt'), 'r') as f:
        return [line.strip() for line in f.readlines()]

def read_subject_marks(directory, files):
    """Зчитує оцінки з кожного предмету та формує словник."""
    subject_marks = {file.replace('.txt', ''): [] for file in files}
    for txt_file in files:
        subject_name = txt_file.replace('.txt', '')
        file_path = os.path.join(directory, txt_file)
        with open(file_path, 'r') as file:
            marks = [int(line.strip()) for line in file.readlines()]
            subject_marks[subject_name].extend(marks)
    return subject_marks

def validate_marks(student_names, subject_marks):
    """Перевіряє відповідність кількості студентів та оцінок."""
    for subject, marks in subject_marks.items():
        if len(marks) != len(student_names):
            raise ValueError(f"Кількість оцінок у {subject} не відповідає кількості студентів.")

def build_student_data(student_names, subject_marks):
    """Створює словник із даними студентів за всіма предметами."""
    return {
        student: {subject: subject_marks[subject][i] for subject in subject_marks}
        for i, student in enumerate(student_names)
    }

def calculate_average_scores(student_data):
    """Розраховує середні оцінки для кожного студента."""
    average_scores = {}
    for student, subjects in student_data.items():
        total_marks = sum(subjects.values())
        average = total_marks / len(subjects)
        average_scores[student] = average
        print(f"Студент: {student}, середня оцінка: {average:.2f}")
    return average_scores

def print_top_students(average_scores, top_n=3):
    """Виводить топ-N студентів за середніми оцінками."""
    print(f"\nТоп-{top_n} студенти за середніми оцінками:")
    top_students = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, (student, avg) in enumerate(top_students, start=1):
        print(f"{i}. {student} з середньою оцінкою: {avg:.2f}")

def print_subject_stats(subject_marks, student_names):
    """Виводить середню, мінімальну та максимальну оцінки для кожного предмету."""
    for subject, marks in subject_marks.items():
        avg = sum(marks) / len(marks)
        min_mark = min(marks)
        max_mark = max(marks)
        print(f"\nПредмет: {subject}, середня оцінка: {avg:.2f}, min оцінка: {min_mark}, max оцінка: {max_mark}")

        # Знаходження студента з найвищою оцінкою
        max_student = student_names[marks.index(max_mark)]
        print(f"Предмет: {subject} | Студент: {max_student}, оцінка: {max_mark}")

def print_low_score_students(average_scores, threshold=50):
    """Виводить студентів із середньою оцінкою нижче заданого порогу."""
    low_score_students = [student for student, avg in average_scores.items() if avg < threshold]
    print(f"\nКількість студентів з середньою оцінкою нижче {threshold}: {len(low_score_students)}")
    for student in low_score_students:
        print(student)

def main():
    """Основна функція для запуску всіх операцій."""
    directory = 'student_marks'
    files = get_files(directory)
    student_names = read_student_names(directory)
    subject_marks = read_subject_marks(directory, files)
    
    validate_marks(student_names, subject_marks)
    
    student_data = build_student_data(student_names, subject_marks)
    average_scores = calculate_average_scores(student_data)
    
    print_top_students(average_scores)
    print(f"\nЗагальна кількість студентів: {len(student_names)}")
    print_subject_stats(subject_marks, student_names)
    print_low_score_students(average_scores)

# Запуск програми
if __name__ == "__main__":
    main()

