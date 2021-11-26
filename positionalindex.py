import os
import re   
import json    

os.chdir("dataset")

pattern = re.compile(r'''(?x)       # set flag to allow verbose regexps
	        ([A-Z]\.)+              # abbreviations
        |   \$?\d+(\.\d+)?%?        # currency and percentages,
        |   \w+                     # words 
 ''',re.VERBOSE | re.I)

index = dict()

files = os.listdir()

for j in range(0,len(files)):
    doc_id = j+1
    f = open(files[j],'r',encoding='utf8')
    words = pattern.finditer(f.read())
    pos=1
    for word in words:
        word = word.group().lower()
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
    f.close()            

os.chdir("..")

with open('positional_index.json','w',encoding='utf-8') as file:
    json.dump(index,file,indent=4)
    file.close()    

print('No of words in the positional index {}'.format(len(index)))