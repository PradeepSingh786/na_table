def na_table(data):
    import pandas as pd
    na_table=pd.DataFrame()
    na_table['Total NA']=data.isna().sum()
    na_table['Percent NA']=round(data.isna().sum()/data.isna().count()*100,2)

    return na_table
# yeah that's great programme you made.
