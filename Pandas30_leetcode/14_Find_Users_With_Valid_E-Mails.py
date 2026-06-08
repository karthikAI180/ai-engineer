import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    filt=users['mail'].str.contains('^[A-Za-z]+[\w.-]*@leetcode\.com$')==True
    return users.loc[filt]
    