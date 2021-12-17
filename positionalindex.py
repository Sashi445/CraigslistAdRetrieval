import os
import re   
import json 
# import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

os.chdir("dataset")

pattern = re.compile(r'''(?x)       # set flag to allow verbose regexps
	        ([A-Z]\.)+              # abbreviations
        |   [\$|Rs]?\d+(\.\d+)?%?   # currency and percentages,
        |   \w+                     # words 
 ''',re.VERBOSE | re.I)

index = dict()
word_count = dict()
max_tfs = dict()

files = os.listdir()

for j in range(0,3):
    doc_id = j+1
    f = open(files[j],'r',encoding='utf8')
    file_string = f.read()
    words = pattern.finditer(file_string)
    pos=1
    for word in words:
        # word = ps.stem(word.group().lower())
        word = word.group().lower()
        if word in stop_words:
            continue
        if word not in index.keys():
            index[word] = { 'document_count' : 1 , 'documents' : { str(doc_id):{ 'word_count':1 , 'positions':[pos] } } }
        else:
            if doc_id not in index[word]['documents'].keys():
                index[word]['document_count']+=1
                index[word]['documents'][str(doc_id)] = {'word_count':1 , 'positions':[pos]}
            else:
                index[word]['documents'][str(doc_id)]['word_count'] += 1
                index[word]['documents'][str(doc_id)]['positions'].append(pos) 
        pos+=1

    max_tf = 0

    for word in pattern.finditer(file_string):
        word =  word.group().lower()
        if word in stop_words:
            continue
        print(index[word]['documents'][str(doc_id)]['positions'])
        term_freq = len(index[word]['documents'][str(doc_id)]['positions'])
        print(term_freq)
        if max_tf < term_freq:
            max_tf = term_freq

    word_count[j+1] = max_tf       
    f.close()            

os.chdir("..")

with open('positional_index.json','w',encoding='utf-8') as f:
    json.dump(index,f,indent=4)
    f.close() 

with open('word-count.json','w',encoding='utf-8') as f:
    json.dump(word_count,f,indent=4)
    f.close()        

print('No of words in the positional index {}'.format(len(index)))