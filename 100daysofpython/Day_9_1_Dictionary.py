student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for k in student_scores:
    if student_scores[k] >90:
        student_grades[k] = "Outstanding"
    elif student_scores[k] >80:
        student_grades[k] = "Exceeeds Expectations"  
    elif student_scores[k] >70:
        student_grades[k] = "Acceptable"
    else:
        student_grades[k] = "Fail"
    
# 🚨 Don't change the code below 👇
print(student_grades)





