def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    k = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    
    # Add a column with max salary per department
    k['max_salary'] = k.groupby('departmentId')['salary'].transform('max')
    #k
    
    # Keep only rows where salary equals max_salary for that department
    result = k[k['salary'] == k['max_salary']]
    
    # Select and rename columns
    result = result[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result