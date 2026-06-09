import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    k=actor_director.groupby(['actor_id','director_id']).size().reset_index(name='cnt')
    filt=k['cnt']>=3
    return k.loc[filt,['actor_id','director_id']]
    