
# the main function to handle student grades
def student_grades(std_grads):
    if std_grads:
        # count the total students
        total_students = len(std_grads)
        print(total_students)
        
        # find sum of all grades through loop
        sum_of_all_students_grades = 0
        for x in std_grads:
            sum_of_all_students_grades += std_grads[x]

        print(sum_of_all_students_grades)
        
        grades = std_grads.values()
        sum_of_grades = sum(grades)
        length_of_grades = len(grades)

        #  find the average of grades
        average_grade = sum_of_all_students_grades / length_of_grades
        print(average_grade)

        # find the highest grades student
        highest_grades_std_name = max(std_grads, key=std_grads.get)
        # find the lowest grades student
        lowest_grades_std_name = min(std_grads, key=std_grads.get)

        # print the highest and lowest grades students
        print(f"The student with the highest grade is {highest_grades_std_name} with a score of {std_grads[highest_grades_std_name]}.")
        print(f"The student with the lowest grade is {lowest_grades_std_name} with a score of {std_grads[lowest_grades_std_name]}.")

        # store average and total students in a tuple
        average_and_count = (average_grade, total_students)

        students_record = {
            "Average Grade": average_grade,
            "Number of Students": total_students,
            highest_grades_std_name: std_grads[highest_grades_std_name],
            lowest_grades_std_name: std_grads[lowest_grades_std_name]
        }

        return (
            students_record, average_and_count
        )

    else:
        print("No students given")

   
sg = {
 "rafi": 80,
 "hamza": 70,
 "ali": 75
}

result = student_grades(sg)
print(result)
print('Student ID - 100536294')