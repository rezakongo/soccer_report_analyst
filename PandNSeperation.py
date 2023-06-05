import pandas as pd

positive_sents=[]
negative_sents=[]

sents_df=pd.read_csv("./data/sentencebroken/result.csv")
players_col=[]
ratings_col=[]
sents_col=[]
for c in list(sents_df.columns):
    if(c[0]=='r'):
        ratings_col.append(c)
    elif(c[0]=='p'):
        players_col.append(c)
    elif(c[0]=='s'):
        sents_col.append(c)


players_col=len(players_col)
ratings_col=len(ratings_col)
sents_col=len(sents_col)


for row in range(len(sents_df)):
    for i in range(players_col):
        player=sents_df.loc[row,'player'+str(i)]
        rating=sents_df.loc[row,'rating'+str(i)]
        sents=list(sents_df.loc[row,'sent0':'sent'+str(sents_col-1)])
        for sent in sents:
            if(str(type(sent))=="<class 'str'>" and player in sent.split()):
                if(rating=="True"):
                    positive_sents.append(sent)
                elif(rating=="False"):
                    negative_sents.append(sent)


positives_df=pd.DataFrame.from_dict({'sents':positive_sents})
negative_df=pd.DataFrame.from_dict({'sents':negative_sents})

positives_df.to_csv("./data/Seperated_By_Labels/positives.csv")
negative_df.to_csv("./data/Seperated_By_Labels/negatives.csv")
