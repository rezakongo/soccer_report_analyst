import pandas as pd

df=pd.read_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/result.csv')
df=df.loc[df['report'].str.len() > 10]
df=df.loc[df['ratings'].str.len() >10]
df = df.reset_index()
df=df.loc[:,['report','ratings']]
df.to_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/clean/result.csv')