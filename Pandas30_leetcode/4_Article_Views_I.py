import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filt=views['author_id']==views['viewer_id']
    views=views[filt][['author_id']]
    views=views.drop_duplicates()
    views = views.sort_values('author_id')
    return views[['author_id']].rename(columns={'author_id':'id'})



    
 
    
    