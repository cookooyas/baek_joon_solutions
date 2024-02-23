import sys
grades = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}
credit_sum = 0
grade_sum = 0
while 1:
    try:
        lecture, credit, grade = sys.stdin.readline().split()
        if grade != 'P':
            credit_sum += int(credit[0])
            grade_sum += int(credit[0]) * grades[grade]
    except:
        break
print(grade_sum / credit_sum)
