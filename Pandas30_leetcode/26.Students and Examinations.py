import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Cross join (all combinations of students × subjects)
    result = students.merge(subjects, how='cross')
    # Step 2: Group exams by student_id and subject_name, count
    exams_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    # Step 3: Left merge with exam counts
    result = result.merge(exams_count, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'].fillna(0,inplace=True)

    # print(j)
    return result.sort_values(['student_id','subject_name'])
    