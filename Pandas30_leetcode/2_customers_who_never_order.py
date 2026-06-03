import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filt = ~customers['id'].isin(orders['customerId'])
    return customers[filt][['name']].rename(columns={'name': 'Customers'})