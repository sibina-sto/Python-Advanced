def get_student_grades(n):
    students_record = {}

    for _ in range(n):
        name, grade = input().split()
        if name not in students_record:
            students_record[name] = []
        students_record[name] += [float(grade)]

    return students_record


def get_average_grade(grades):
    return sum(grades) / len(grades)


def print_result(students_record):
    for name, grades in students_record.items():
        average_grade = get_average_grade(grades)
        formatted_grades = ' '.join([f'{grade:.2f}' for grade in grades])
        print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")


n = int(input())
print_result(get_student_grades(n))
