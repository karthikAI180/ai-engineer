import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   
    # red_id = company[company['name'] == 'RED']['com_id'].values
    # red_salespeople = orders[orders['com_id'].isin(red_id)]['sales_id'].unique()
    # return sales_person[~sales_person['sales_id'].isin(red_salespeople)][['name']]
    k=orders.merge(company,on='com_id',how='left')
    j=k.merge(sales_person,on='sales_id',how='right')
    j=j.loc[:,['name_x','name_y']]
    j=j.groupby('name_y')['name_x'].apply(list).reset_index()
    # If name_x contains LISTS with color names:
    j = j[~j['name_x'].apply(lambda x: 'RED' in x if isinstance(x, list) else False)]
    


    

    return j.loc[:,['name_y']].rename(columns={'name_y':'name'})
  
    