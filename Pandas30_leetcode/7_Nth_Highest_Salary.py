import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values('salary',ascending=False,inplace=True)
    employee['rank']=employee['salary'].rank(method='dense',ascending=False)
    if N<=0 or N>employee['rank'].max():
         return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    filt=employee['rank']==N
    return employee[filt][['salary']].iloc[0:1].rename(columns={'salary':f'getNthHighestSalary({N})'})
    