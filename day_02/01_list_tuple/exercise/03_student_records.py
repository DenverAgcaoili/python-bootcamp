student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
student_data = zip(student_names,student_scores)
# indices = [0,1,2]
for student_name,student_score in student_data:
    print(f"{student_name} scored {student_score} in the exam")
