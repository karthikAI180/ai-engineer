import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    k=employee_uni.merge(employees,on='id',how='right')
    return k[['unique_id','name']]
    