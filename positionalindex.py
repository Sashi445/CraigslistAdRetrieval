import os
import re   
import json 
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
    document = {}

    for word in words:
        # word = ps.stem(word.group().lower())
        word = word.group().lower()
        if word in stop_words:
            continue
        if word not in document.keys():
            document[word] = {'word_count':1 , 'positions':[pos]}
        else:
            document[word]['word_count'] +=1
            document[word]['positions'].append(pos)
        pos+=1

    for word in document.keys():
        if word not in index.keys():
            index[word] = { 'document_count' : 1 , 'documents' : { str(doc_id): document[word] } }
        else:
            index[word]['document_count']+=1
            index[word]['documents'][str(doc_id)] = document[word]   

    word_count[str(doc_id)] = max([document[word]['word_count'] for word in document.keys()])             

    f.close()            

os.chdir("..")

with open('positional_index.json','w',encoding='utf-8') as f:
    json.dump(index,f,indent=4)
    f.close() 

with open('word-count.json','w',encoding='utf-8') as f:
    json.dump(word_count,f,indent=4)
    f.close()        

print('No of words in the positional index {}'.format(len(index)))