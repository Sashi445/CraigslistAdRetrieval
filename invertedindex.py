import os
import re   
import json    

os.chdir("dataset")

pattern = re.compile(r'''(?x)       # set flag to allow verbose regexps
	        ([A-Z]\.)+              # abbreviations
        |   [\$|Rs]?\d+(\.\d+)?%?   # currency and percentages,
        |   \w+                     # words 
 ''',re.VERBOSE | re.I)

index = dict()

files = os.listdir()

fnames = list()
for f in os.listdir():
    id = f.split(".")[0]
    fnames.append(id)


for j in range(0,len(files)):
    doc_id = j+1
    f = open(files[j],'r',encoding='utf8')
    words = pattern.finditer(f.read())
    temp = set(words)
    for word in temp:
        word = word.group().lower()
        if word not in index.keys():
            index[word]={fnames.index(fnames[j])+1:1}
        else:
            if fnames.index(fnames[j])+1 not in index[word].keys():
                index[word][fnames.index(fnames[j])+1] = 1
            else:
                index[word][fnames.index(fnames[j])+1] += 1

    f.close()   

for k,v in index.items():
    v = list(v.items())
    print(v)
    index[k] = v

os.chdir("..")

with open('inverted_index.json','w',encoding='utf-8') as f:
    json.dump(index,f,indent=4)
    f.close()    

# print('No of words in the inverted index {}'.format(len(index)))