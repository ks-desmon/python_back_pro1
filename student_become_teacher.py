
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students =[lloyd,alice,tyler]
def average(numbers):
    total=sum(numbers)
    total=float(total)/len(numbers)
    return total
def get_average(students):
    homework=(average(students["homework"])*10)/100
    quizzes=(average(students["quizzes"])*30)/100
    tests=(average(students["tests"])*60)/100
    return homework+quizzes+tests
# Add your function below!
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))
def get_class_average(students):
    result=[]
    avg=0
    for student in students:
        result.append(get_average(student))
    return average(result)
print get_class_average(students)

