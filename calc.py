from tkinter import N


def AverageGrade(grades):
    average_grade = 0.0
    num_of_classes = 0

    for grade in grades:
        if grade != 'No Grade':
            average_grade += float(grade[:-1])
            num_of_classes += 1
        else:
            continue

    return "Average Grade: " + str(round(average_grade/num_of_classes, 2))


def Grade_Class_Organizer(grades, classes):
    classAndGrades = []

    if len(grades) == len(classes):
        for i in range(len(grades)):
            classAndGrades.append("Class: " + classes[i] + " Grade: " + grades[i])
            # print("Class: " + classes[i])
            # print("Grade: " + grades[i])
    else:
        return "Nothing is here."

    return classAndGrades
            
