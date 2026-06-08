import pandas as pd
def cat(income):
    if income<20000:
        return 'Low Salary' 
    elif income >=20000 and income<=50000:
        return 'Average Salary'
    elif income>50000:
        return 'High Salary'
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category']=accounts['income'].apply(cat)
    result = accounts['category'].value_counts().reindex(
        ['Low Salary', 'Average Salary', 'High Salary'], 
        fill_value=0
    ).reset_index()
    print(result)
    # result.rename(columns={'count':'accounts_count'},inplace=True)->This approch has More rum time. So, its not preferred
    result.columns = ['category', 'accounts_count']
    return result
    