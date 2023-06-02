import pandas as pd

pad_token='<PAD>'

def break_sents(report):
    sents=report.split('.')
    return sents

def break_words(report):
    words=report.split(' ')
    return words

def get_rated_players(ratings):
    ratings=ratings.replace(' ', '')
    ratings=ratings.replace('.', '')
    ratings=ratings.replace('\n','')
    ratings=ratings.replace(',', '')
    ratings=ratings.replace(';', '')
    ratings=ratings.replace(')', '),')
    ratings=ratings.split(',')

    na_players=[]
    for p in ratings:
        if("N/A" in p):
            na_players.append(p)

    for p in ratings:
        if("n/a" in p):
            na_players.append(p)

    for p in ratings:
        if(len(p)<4 or p[-1]!=')' or p[-3]!='('):
            na_players.append(p)
        if(len(p)>1 and (not p[-2].isdigit())):
            na_players.append(p)

    na_players=list(set(na_players))
    for p in na_players:
        while(p in ratings):
            ratings.remove(p)
    
    players_rates={
        'players':[],
        'ratings':[]
    }

    for p in ratings:
        players_rates['players'].append(p[:-3])
        try:
            players_rates['ratings'].append(int(p[-2])>6)
        except:
            print(na_players)
            print(ratings)
            exit()

    return players_rates

df=pd.read_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/clean/result.csv')
df=df[['report','ratings']]


max_len=max([len(break_sents(r)) for r in df['report']])
max_words=max([len(break_words(r)) for r in df['report']])
max_players=max([len(get_rated_players(r)['players']) for r in df['ratings']])

players={}
columns={}
words_columns={}

for i in range(0,max_len):
    columns['sent'+str(i)]=[]
    
for i in range(0,max_words):
    words_columns['word'+str(i)]=[]

for i in range(0,max_players):
    players['player'+str(i)]=[]
    players['rating'+str(i)]=[]

for index,row in df.iterrows():
    r=row['ratings']
    r=get_rated_players(r)
    report=row['report']
    report=break_sents(report)
    report_words=row['report']
    report_words=break_words(report_words)
    for i in range(0,max_len):
        if(i>=len(report)):
            columns['sent'+str(i)].append(pad_token)
        else:
            columns['sent'+str(i)].append(report[i])
    
    for i in range(0,max_words):
        if(i>=len(report_words)):
            words_columns['word'+str(i)].append(pad_token)
        else:
            words_columns['word'+str(i)].append(report_words[i])

    for i in range(0,max_players):
        if(i>=len(r['players'])):
            players['player'+str(i)].append(pad_token)
            players['rating'+str(i)].append(pad_token)
        else:
            players['player'+str(i)].append(r['players'][i])
            players['rating'+str(i)].append(r['ratings'][i])
            
    
columns.update(players)
words_columns.update(players)
df=pd.DataFrame.from_dict(columns)
df.to_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/sentencebroken/result.csv')
df=pd.DataFrame.from_dict(words_columns)
df.to_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/wordbroken/result.csv')

