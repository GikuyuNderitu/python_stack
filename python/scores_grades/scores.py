def get_grade(x):
	grade = int(raw_input('Get grade: '))
	while grade < 60 or grade > 100:
		grade = int(raw_input('I\'m sorry, that was an invalid input value. Please insert a number between 60 and 100 (inclusive): '))

	return grade

# returns an array of grades
def get_grades(num):
	grades = []
	for val in range(1,num+1):
		grades.append(get_grade(val))
	return grades

def printGrades(arr):
	print 'Scores and Grades'
	for val in arr:
		print 'Score:',val,'Your grade is: ',evalGrade(val)

def evalGrade(grade):
	if grade >= 90:
		return 'A'
	elif grade >= 80:
		return 'B'
	elif grade >= 70:
		return 'C'
	else:
		return 'D'

gradeArr = get_grades(5)
printGrades(gradeArr)
