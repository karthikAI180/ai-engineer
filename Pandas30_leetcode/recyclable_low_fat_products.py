import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filt = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products[filt][['product_id']]