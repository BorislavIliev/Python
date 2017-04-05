universities = []


def enrollment_stats():
    total_tuitions = 0
    total_students = 0
    students_mean = 0
    tuitions_mean = 0
    for i in range(1, 3):
        new_list = input().split()
        universities.append(new_list)
        new_list = []
    for i in range(0, len(universities)):
        total_students += int(universities[i][1])
        total_tuitions += float(universities[1][2])
    print('********************* \n', 'Total students: ', total_students)
    return total_students, total_tuitions, universities


def mean():
    total_students = 0
    total_tuitions = 0
    for i in range(0, len(universities)):
        total_students += int(universities[i][1])
        total_tuitions += int(universities[i][2])
    tuitions_mean = total_tuitions / 2
    students_mean = total_students / 2
    print(" Students mean: ", students_mean, "\n", "Tuitions mean: ", tuitions_mean)

enrollment_stats()
mean()