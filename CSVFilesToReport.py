import pandas as pd

urls=pd.read_csv("./data/row/data_sources.csv")
urls=urls[:10]
urls.to_csv("./Document/urls.csv")

row_datas=pd.read_csv("./data/row/result.csv")
row_datas=row_datas[:10]
row_datas.to_csv("./Document/row_data.csv")

clean_datas=pd.read_csv("./data/clean/result.csv")
clean_datas=row_datas[:10]
clean_datas.to_csv("./Document/clean_data.csv")

s_datas=pd.read_csv("./data/sentencebroken/result.csv")
s_datas=s_datas.loc[:10,'sent132':'rating0']
s_datas.to_csv("./Document/sentence_broken_data.csv")

w_datas=pd.read_csv("./data/wordbroken/result.csv")
w_datas=w_datas.loc[:10,'word2249':'rating0']
w_datas.to_csv("./Document/word_broken_data.csv")

n_datas=pd.read_csv("./data/Seperated_By_Labels/negatives.csv")
n_datas=n_datas[:10]
n_datas.to_csv("./Document/negative_data.csv")

p_datas=pd.read_csv("./data/Seperated_By_Labels/positives.csv")
p_datas=p_datas[:10]
p_datas.to_csv("./Document/positive_data.csv")