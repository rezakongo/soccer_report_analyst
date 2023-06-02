import pandas as pd

words_df=pd.read_csv('data/wordbroken/result.csv')
sents_df=pd.read_csv('data/sentencebroken/result.csv')
words_df_cols=[]
sents_df_cols=[]
players_cols=[]
for c in words_df.columns:
    if(c[0]=='w'):
        words_df_cols.append(c)

for c in sents_df.columns:
    if(c[0]=='s'):
        sents_df_cols.append(c)
    if(c[0]=='p' or c[0]=='r'):
        players_cols.append(c)

metrics={
    'words':[],
    'u_words':[],
    'sents':[]
}
for i in range(0,10):
    metrics['word'+str(i+1)]=[]
    metrics['word_count'+str(i+1)]=[]

words_df=words_df.loc[:,words_df_cols]
total_df=pd.concat([words_df,sents_df], axis=1)
#total_df=total_df.loc[:20,:]
for i,r in  total_df.iterrows(): 
    words=list(total_df.loc[i,words_df_cols])
    while '<PAD>' in words:
        words.remove('<PAD>')
    
    u_words=list(set(words))
    words_counter={}
    for w in u_words:
        words_counter[w]=words.count(w)
    print(words_counter)
    max_words=dict(sorted(words_counter.items(),key=lambda x: x[1],reverse=True))
    max_words=list(max_words.keys())[:10]
    words_counter={}
    print(max_words)
    for w in max_words:
        words_counter[w]=words.count(w)

    print("mmd"+str(words_counter))
    for j in range(0,10):
        metrics['word'+str(j+1)].append(list(words_counter.keys())[j])
        metrics['word_count'+str(j+1)].append(list(words_counter.values())[j])
    sents=list(total_df.loc[i,sents_df_cols])
    while '<PAD>' in sents:
        sents.remove('<PAD>')
    
    metrics['words'].append(len(words))
    metrics['u_words'].append(len(u_words))
    metrics['sents'].append(len(sents))
    print(str(i)+' : Success!')

substitutions=sents_df.loc[:,players_cols]
metrics=pd.concat([substitutions,pd.DataFrame.from_dict(metrics)],axis=1)
metrics.to_csv('metrics/metrics.csv')