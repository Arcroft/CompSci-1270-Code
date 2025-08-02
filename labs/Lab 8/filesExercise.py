# Ashlyn Croft
# 20JUL25
# Lab 8
# Files Excersize
# Pulling from students.txt to give descriptive statistics





def readStudents(filename):
    """
    Reads the students.txt file and returns a list of (student_id, name)
    """
    students = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            parts = line.strip().split(', ')
            student_id = parts[0].strip()
            name = parts[1].strip()
            students.append((student_id, name))
    
    return students







def readScores(filename):
    """
    Reads the scores.txt file and returns a list of (student_id, assignment, score)
    """
    scores = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            parts = line.strip().split(', ')
            student_id = parts[0].strip()
            assignment = parts[1].strip()
            score = int(parts[2].strip())
            scores.append((student_id, assignment, score))
    
    return scores





def calculateGrades(students, scores):
    """
    Calculates grade statistics for each student.
    """
    # master grades list with column headers
    grades = [["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]]
    
    # Process each student
    for student_id, name in students:
        student_scores = []
        for score_student_id, assignment, score in scores:
            if score_student_id == student_id:
                student_scores.append(score)
        
        # Calculate statistics
        if student_scores:
            total_scores = len(student_scores)
            sum_scores = sum(student_scores)
            score_average = sum_scores / total_scores
            
            # grade list for student
            calculated_grade = [student_id, name, total_scores, sum_scores, score_average]
            
            # Append to grades list
            grades.append(calculated_grade)
    
    return grades






def writeGrades(grades, filename):
    """
    Writes the grades data to a file in format specified.
    """

    with open(filename, 'w') as f:
        for i, row in enumerate(grades):
            if i == 0: 
                formatted_row = ','.join(row)
            else:
                student_id, name, total_scores, sum_scores, score_average = row
                formatted_row = f"{student_id},{name},{total_scores},{sum_scores},{score_average:.1f}"
            
            f.write(formatted_row)
            

            if i < len(grades) - 1:
                f.write('\n')






def main():
    """
    Main function - coordinates the grade calculation process.
    """
    print("Student Grade Calculator")
    print("=" * 40)
    print("This program processes student and score data using relational database concepts.")
    print("Students.txt contains the primary key (Student ID) and student names.")
    print("Scores.txt contains foreign key references and assignment scores.")
    print()
    
    try:
        # Read the student data
        students = readStudents('students.txt')
        print(f"Loaded {len(students)} students from students.txt")
        

        # Read the scores data
        scores = readScores('scores.txt')
        print(f"Loaded {len(scores)} score records from scores.txt")
        

        # Calculate grade statistics
        grades = calculateGrades(students, scores)
        print(f"Calculated grades for {len(grades)-1} students") 
        
        
        # Write results to output
        writeGrades(grades, 'grades.txt')
        print("Grade analysis saved to grades.txt")
        
        # Display summary statistics

    
        print("\nGrade Summary:")
        print("-" * 30)
        for i, row in enumerate(grades):
            if i == 0:
                continue
            student_id, name, total, sum_val, avg = row
            print(f"{name}: {total} assignments, average: {avg:.1f}")
        
    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e}")
        print("Make sure both students.txt and scores.txt are in the same folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


# This one is not as magically interesting.
# Or I'm too tired and exhausted brain reserves.

# Used ctrl z alot. Best thing I've learned for python.