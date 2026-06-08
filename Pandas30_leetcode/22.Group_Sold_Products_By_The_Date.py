import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    k=activities.groupby('sell_date')['product'].apply(lambda x: ','.join(sorted(x.unique()))).reset_index(name='products')
    # k['num_sold']=k['products'].apply(lambda x: len(x.split(','))) ->not much effeicent
    k['num_sold'] = k['products'].str.count(',') + 1

    cols=list(k.columns)
    # k=k[[cols[0]+cols[2]+cols[1]]]
    k=k[[cols[0], cols[2], cols[1]]]  # Use double brackets + list
    return k
    