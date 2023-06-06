from datasets import load_dataset
from datasets import Dataset
import pandas as pd

sents_df=pd.read_csv("./data/sentencebroken/result.csv")
sents_df=Dataset.from_pandas(sents_df)
sents_df.push_to_hub("ParsaKgvr/socce_report_analysis")