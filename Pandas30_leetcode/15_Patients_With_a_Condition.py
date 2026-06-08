import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    filt=patients['conditions'].str.contains(r'(^| )DIAB1', regex=True)
    return patients.loc[filt]
    