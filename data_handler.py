import os

def get_student_names(directory):
    """
    Зчитує та повертає список імен студентів із файлу student_names.txt.

    Args:
        directory (str): Шлях до директорії з файлом student_names.txt.

    Returns:
        list: Список імен студентів.
    """
    with open(os.path.join(directory, 'student_names.txt'), 'r') as f:
        return [line.strip() for line in f.readlines()]

def get_subject_files(directory):
    """
    Повертає список файлів предметів, виключаючи student_names.txt.

    Args:
        directory (str): Шлях до директорії.

    Returns:
        list: Список файлів предметів.
    """
    return [file for file in os.listdir(directory) 
            if file.endswith('.txt') and file != 'student_names.txt']

def read_subject_marks(files, directory):
    """
    Зчитує оцінки з файлів предметів та повертає їх у вигляді словника.

    Args:
        files (list): Список файлів предметів.
        directory (str): Шлях до директорії з файлами.

    Returns:
        dict: Словник із предметами та їхніми оцінками.
    """
    subject_marks = {file.replace('.txt', ''): [] for file in files}
    for txt_file in files:
        subject_name = txt_file.replace('.txt', '')  
        file_path = os.path.join(directory, txt_file)
        with open(file_path, 'r') as file:
            marks = [int(line.strip()) for line in file.readlines()]
            subject_marks[subject_name].extend(marks)
    return subject_marks

def validate_data(student_names, subject_marks):
    """
    Перевіряє відповідність кількості студентів кількості оцінок у кожному предметі.

    Args:
        student_names (list): Список імен студентів.
        subject_marks (dict): Словник із предметами та їхніми оцінками.

    Raises:
        ValueError: Якщо кількість оцінок не відповідає кількості студентів.
    """
    for subject, marks in subject_marks.items():
        if len(marks) != len(student_names):
            raise ValueError(f"Кількість оцінок у {subject} не відповідає кількості студентів.")

def create_student_data(student_names, subject_marks):
    """
    Створює словник із оцінками для кожного студента за всі предмети.

    Args:
        student_names (list): Список імен студентів.
        subject_marks (dict): Словник із предметами та їхніми оцінками.

    Returns:
        dict: Словник з оцінками для кожного студента.
    """
    return {
        student: {subject: subject_marks[subject][i] for subject in subject_marks}
        for i, student in enumerate(student_names)
    }

def print_student_data(student_data):
    """
    Виводить у консоль дані про кожного студента та обчислює середні оцінки.

    Args:
        student_data (dict): Словник із даними студентів.
    """
    for student, subjects in student_data.items():
        print(f"Ім'я студента: {student}")
        print("Оцінки з предметів:")
        total_marks = 0

        for subject, mark in subjects.items():
            print(f"{subject}: {mark}")
            total_marks += mark

        average = total_marks / len(subjects)
        print(f"Середнє значення оцінок: {average:.2f}")
        print("-" * 30)

def main():
    """
    Основна функція програми, яка виконує весь процес зчитування та виведення даних.
    """
    directory = 'student_marks'
    student_names = get_student_names(directory)
    subject_files = get_subject_files(directory)
    subject_marks = read_subject_marks(subject_files, directory)
    
    validate_data(student_names, subject_marks)
    student_data = create_student_data(student_names, subject_marks)
    
    print_student_data(student_data)

# Виклик основної функції
if __name__ == "__main__":
    main()

