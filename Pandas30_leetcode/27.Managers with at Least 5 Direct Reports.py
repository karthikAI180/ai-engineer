import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    k = employee.groupby('managerId')['name'].apply(list).reset_index()
    k['count'] = k['name'].apply(len)
    k = k[k['count'] >= 5]
    return employee[employee['id'].isin(k['managerId'])][['name']]
    