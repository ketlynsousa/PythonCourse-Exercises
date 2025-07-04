# Python Exercise 104 - Validating data input in Python
# Write a program that has a function grades() that can receive several grades from students
# and will return a dictionary with the following information:
# - Number of grades
# - The highest grade
# - The lowest grade
# - The class average
# - The situation (optional)
# Also add the docstrings of this function for consultation by the developer.
def grades(* num, sit=False):
    """
    Function to analyze the grade of several students and optionally show the student's situation.
    :param num: It can receive an unlimited amount of students' grades.
    :param sit: the optional value will return the students' situation.
    :return: returns dictionary with basic metrics about grades.
    """
    d = dict()
    d['Total'] = len(num)
    d['Biggest'] = max(num)
    d["Smallest"] = min(num)
    d['Average'] = sum(num) / len(num)
    if sit:
        if d['Average'] >= 7:
            d['Situation'] = 'GOOD'
        elif d['Average'] >= 5:
            d['Situation'] = 'REASONABLE'
        else:
            d['Situation'] = 'BAD'
    return d


# Programa principal
answer = grades(4.5, 5.0, 7.1, 9, sit=True)
print(answer)
print()

answer2 = grades(2.1, 9.1, 3.5, 5.5)
print(answer2)
print()
