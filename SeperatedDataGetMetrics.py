import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    positive_sents=pd.read_csv('./data/Seperated_By_Labels/positives.csv')
    negative_sents=pd.read_csv('./data/Seperated_By_Labels/negatives.csv')
    return positive_sents, negative_sents

def get_sents_n():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    all_sents_n=positive_sents_n+negative_sents_n

    print("Number of positive sents: "+str(positive_sents_n)+"\tNumber of negative sents: "+str(negative_sents_n)+"\tNumber of all sents: "+str(all_sents_n))
    return positive_sents_n, negative_sents_n, all_sents_n


def get_words_n():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)
    
    positive_words_n=len(positive_words)
    negative_words_n=len(negative_words)
    all_words_n=positive_words_n+negative_words_n
    print("Number of positive words: "+str(positive_words_n)+"\tNumber of negative words: "+str(negative_words_n)+"\tNumber of all words: "+str(all_words_n))
    return positive_words_n,negative_words_n,all_words_n

def get_unique_words_n():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]
    all_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)
            all_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)
            all_words.append(word)
    
    positive_words_n=len(list(set(positive_words)))
    negative_words_n=len(list(set(negative_words)))
    all_words_n=len(list(set(all_words)))
    
    print("Number of unique positive words: "+str(positive_words_n)+"\tNumber of unique negative words: "+str(negative_words_n)+"\tNumber of unique all words: "+str(all_words_n))
    return positive_words_n,negative_words_n,all_words_n

def get_union_intersection_words_n():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)

    positive_words=set(positive_words)
    negative_words=set(negative_words)
    
    positive_words_n=len(list(positive_words-negative_words))
    negative_words_n=len(list(negative_words-positive_words))
    intersected_words_n=len(list(positive_words.intersection(negative_words)))

    
    print("Number of only positive words: "+str(positive_words_n)+"\tNumber of only negative words: "+str(negative_words_n)+"\tNumber of intersected words: "+str(intersected_words_n))
    return positive_words_n,negative_words_n,intersected_words_n

def get_10_unique_words():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)

    positive_words_set=set(positive_words)-set(negative_words)
    negative_words_set=set(negative_words)-set(positive_words)

    positive_words_count={}
    negative_words_count={}

    
    for p_w in list(positive_words_set):
        positive_words_count[p_w]=positive_words.count(p_w)
    
    for n_w in list(negative_words_set):
        negative_words_count[n_w]=negative_words.count(n_w)

    top_10_negative_words=list(dict(sorted(negative_words_count.items(),key=lambda x:x[1],reverse=True)).keys())[:10]
    top_10_positive_words=list(dict(sorted(positive_words_count.items(),key=lambda x:x[1],reverse=True)).keys())[:10]

    top_10_negative_words_count=[negative_words_count[word] for word in top_10_negative_words]
    top_10_positive_words_count=[positive_words_count[word] for word in top_10_positive_words]

    plt.barh(top_10_negative_words,top_10_negative_words_count)
    plt.savefig("./metrics/top10NegativeWordsCount")

    plt.close()
    plt.barh(top_10_positive_words,top_10_positive_words_count)
    plt.savefig("./metrics/top10PositiveWordsCount")

    print("Top 10 positive words: "+str(top_10_positive_words)+"\tTop 10 negative words: "+str(top_10_negative_words))
    return top_10_positive_words, top_10_negative_words


def get_10_common_words():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)

    common_words_set=set(positive_words).intersection(set(negative_words))

    common_positive_words_count={}
    common_negative_words_count={}
    common_positive_words_frequency={}
    common_negative_words_frequency={}

    
    for word in list(common_words_set):
        common_positive_words_count[word]=positive_words.count(word)
        common_negative_words_count[word]=negative_words.count(word)
    
    for word in list(common_words_set):
        common_positive_words_frequency[word]=(common_positive_words_count[word]/sum(common_positive_words_count.values()))/(common_negative_words_count[word]/sum(common_negative_words_count.values()))
        common_negative_words_frequency[word]=(common_negative_words_count[word]/sum(common_negative_words_count.values()))/(common_positive_words_count[word]/sum(common_positive_words_count.values()))
        

    top_10_negative_words=list(dict(sorted(common_negative_words_frequency.items(),key=lambda x:x[1],reverse=True)).keys())[:10]
    top_10_positive_words=list(dict(sorted(common_positive_words_frequency.items(),key=lambda x:x[1],reverse=True)).keys())[:10]
    top_10_negative_words_frequency=[common_negative_words_frequency[word] for word in top_10_negative_words]
    top_10_positive_words_frequency=[common_positive_words_frequency[word] for word in top_10_positive_words]

    plt.close()
    plt.barh(top_10_negative_words,top_10_negative_words_frequency)
    plt.savefig("./metrics/top10CommonNegativeWordsFrequency")

    plt.close()
    plt.barh(top_10_positive_words,top_10_positive_words_frequency)
    plt.savefig("./metrics/top10CommonPositiveWordsFrequency")
    
    print("Top 10 positive words: "+str(top_10_positive_words)+"\tTop 10 negative words: "+str(top_10_negative_words))
    return top_10_positive_words, top_10_negative_words


def get_10_wordsـby_tfidf():
    positive_sents, negative_sents=load_data()
    positive_sents_n=len(positive_sents)
    negative_sents_n=len(negative_sents)
    positive_words=[]
    negative_words=[]

    for i in range(positive_sents_n):
        sent=positive_sents.loc[i,'sents']
        for word in sent.split():
            positive_words.append(word)

    for i in range(negative_sents_n):
        sent=negative_sents.loc[i,'sents']
        for word in sent.split():
            negative_words.append(word)

    positive_words_set=set(positive_words)-set(negative_words)
    negative_words_set=set(negative_words)-set(positive_words)
    positive_words_frequency={}
    negative_words_frequency={}

    for word in list(positive_words_set):
        positive_words_frequency[word]=(positive_words.count(word)/len(positive_words))*np.log(2/1)
    
    for word in list(negative_words_set):
        negative_words_frequency[word]=(negative_words.count(word)/len(negative_words))*np.log(2/1)

    

        

    top_10_negative_words=list(dict(sorted(negative_words_frequency.items(),key=lambda x:x[1],reverse=True)).keys())[:10]
    top_10_positive_words=list(dict(sorted(positive_words_frequency.items(),key=lambda x:x[1],reverse=True)).keys())[:10]
    top_10_negative_words_frequency=[negative_words_frequency[word] for word in top_10_negative_words]
    top_10_positive_words_frequency=[positive_words_frequency[word] for word in top_10_positive_words]

    plt.close()
    plt.barh(top_10_negative_words,top_10_negative_words_frequency)
    plt.savefig("./metrics/top10CommonNegativeWordsTFIDF")

    plt.close()
    plt.barh(top_10_positive_words,top_10_positive_words_frequency)
    plt.savefig("./metrics/top10CommonPositiveWordsTFIDF")
    
    print("Top 10 positive words: "+str(top_10_positive_words)+"\tTop 10 negative words: "+str(top_10_negative_words))
    return top_10_positive_words, top_10_negative_words



result=""
positive_sents_n, negative_sents_n, all_sents_n=get_sents_n()
result+="Number of positive sents: "+str(positive_sents_n)+"\tNumber of negative sents: "+str(negative_sents_n)+"\tNumber of all sents: "+str(all_sents_n)+'\n'

positive_words_n,negative_words_n,all_words_n=get_words_n()
result+="Number of positive words: "+str(positive_words_n)+"\tNumber of negative words: "+str(negative_words_n)+"\tNumber of all words: "+str(all_words_n)+'\n'

positive_words_n,negative_words_n,all_words_n=get_unique_words_n()
result+="Number of unique positive words: "+str(positive_words_n)+"\tNumber of unique negative words: "+str(negative_words_n)+"\tNumber of unique all words: "+str(all_words_n)+'\n'

positive_words_n,negative_words_n,intersected_words_n=get_union_intersection_words_n()
result+="Number of only positive words: "+str(positive_words_n)+"\tNumber of only negative words: "+str(negative_words_n)+"\tNumber of intersected words: "+str(intersected_words_n)+'\n'

top_10_positive_words, top_10_negative_words=get_10_unique_words()
result+="Top 10 positive words: "+str(top_10_positive_words)+"\tTop 10 negative words: "+str(top_10_negative_words)+'\n'

top_10_positive_words, top_10_negative_words=get_10_common_words()
result+="Top 10 Common positive words: "+str(top_10_positive_words)+"\tTop 10 Common negative words: "+str(top_10_negative_words)+'\n'

top_10_positive_words, top_10_negative_words=get_10_wordsـby_tfidf()
result+="Top 10 positive words TFIDF: "+str(top_10_positive_words)+"\tTop 10 negative words TFIDF: "+str(top_10_negative_words)+'\n'

f = open("./metrics/results.txt", "a")
f.truncate(0)
f.write(result)
f.close()