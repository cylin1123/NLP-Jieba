
# coding: utf-8

# In[1]:

import sys
import time
import jieba
import jieba.analyse as jalz
import jieba.posseg as japseg
from pymongo import MongoClient
#jieba.enable_parallel(4)

#t1 = time.time()
jieba.load_userdict("/home/cylin/Code/Jieba/user_dict") #自訂詞庫檔
jieba.analyse.set_stop_words("/home/cylin/Code/Jieba/stopwords")
#sentence = open("/home/cylin/Code/qqq.txt",'rb').read()


def Extract_Tags(sentence):    
    words = jalz.extract_tags(sentence,20)
    print ",".join(words)
    """
    for word in words:
        print word.encode('utf-8')
    """
def CutWords(sentence):
    words = japseg.cut(sentence)
    for word in words:
        if word.flag =='n':
            print("%s , %s"%(word.word,word.flag))
        
def Tokenize_Word(sentence):
    """斷字斷詞"""
    words = jieba.tokenize(sentence)
    for word in words:
        print("%s start %d end %d"%(word[0],word[1],word[2]))      

def main():
    client = MongoClient('localhost',27017)
    db = client.SocialMedia
    News = db.AppleNews
    
    for data in News.find()[0:10]:
        sentence = data['Title']+','+data['Content']
        print data['Title'] 
        print data['NewsLink']
        CutWords(sentence)   


if __name__=='__main__':
    main()

