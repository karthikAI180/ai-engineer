import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    k=courses.groupby('class').size().reset_index(name='cnt')
    filt=k['cnt']>=5
    return k.loc[filt,['class']]
    