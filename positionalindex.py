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

files = os.listdir()

for j in range(0,len(files)):
    doc_id = j+1
    f = open(files[j],'r',encoding='utf8')
    words = pattern.finditer(f.read())
    pos=1
    i = 0
    for word in words:
        i+=1
        word = ps.stem(word.group().lower())
        if word in stop_words:
            continue
        if word not in index.keys():
            index[word] = { 'document_count' : 1 , 'documents' : { doc_id:{ 'word_count':1 , 'positions':[pos] } } }
        else:
            if doc_id not in index[word]['documents'].keys():
                index[word]['document_count']+=1
                index[word]['documents'][doc_id] = {'word_count':1 , 'positions':[pos]}
            else:
                index[word]['documents'][doc_id]['word_count']+=1
                index[word]['documents'][doc_id]['positions'].append(pos)    
        pos+=1
    word_count[j+1] = i       
    f.close()            

os.chdir("..")

with open('positional_index.json','w',encoding='utf-8') as file:
    json.dump(index,file,indent=4)
    file.close() 

with open('word-count.json','w',encoding='utf-8') as file:
    json.dump(word_count,file,indent=4)
    file.close()        

print('No of words in the positional index {}'.format(len(index)))