import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    filt=(employees['employee_id']%2==1) & (~employees['name'].str.contains('^M',regex=True))
    k = {
        'employee_id':employees['employee_id'],
        'bonus': employees['salary'].where(filt, 0)

    }
    return pd.DataFrame(k).sort_values('employee_id')
    
    